
import "dotenv/config";

import express from "express";
import { ChatGroq } from "@langchain/groq";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { Document } from "@langchain/core/documents";
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";
import { StateGraph, START, END, Annotation } from "@langchain/langgraph";
import { QdrantVectorStore } from "@langchain/qdrant";
import { HuggingFaceTransformersEmbeddings } from "@langchain/community/embeddings/huggingface_transformers";
import { QdrantClient } from "@qdrant/js-client-rest";

// ============================================================
// CONFIGURATION
// ============================================================

const PORT = Number(process.env.PORT || 3000);
const MODEL = process.env.GROQ_MODEL || "openai/gpt-oss-120b";
const QDRANT_URL = process.env.QDRANT_URL || "http://localhost:6333";
const COLLECTION = process.env.QDRANT_COLLECTION || "cravio_support_faq";

if (!process.env.GROQ_API_KEY) {
  throw new Error("Please add GROQ_API_KEY to your .env file");
}

const llm = new ChatGroq({
  model: MODEL,
  apiKey: process.env.GROQ_API_KEY,
  temperature: 0,
});

// Built-in LangChain embedding integration.
// The MiniLM model runs locally; no OpenAI API key is needed.
const embeddings = new HuggingFaceTransformersEmbeddings({
  modelName: "Xenova/all-MiniLM-L6-v2",
});

const qdrantClient = new QdrantClient({
  url: QDRANT_URL,
});

// ============================================================
// FAQ AND POLICIES
// ============================================================

const FAQ = `
# Cravio Customer Support FAQ

## General Information
Cravio is a sample food delivery platform connecting customers with local restaurants.
Customers can browse menus, place orders, pay at checkout, and view their order status.

Sample support hours are 9 AM to 9 PM, Monday through Sunday.
Sample support email: support@cravio.example.
These are fictional details for this learning project.

## Ordering
To place an order, choose a restaurant, select food items, add them to your cart,
enter your delivery address, and complete checkout.
Menu prices and item availability are those displayed in the application.

## Delivery
Delivery time depends on restaurant preparation, distance, traffic, weather,
and rider availability. Check the application for the latest estimate.
Address changes may not be possible after an order is confirmed or preparation begins.

The AI must not invent an order status or claim to have checked live tracking.

## Payments
Available payment methods are displayed during checkout.
If money was deducted but the order was not confirmed, keep the transaction reference
and contact support.
For possible duplicate charges, contact support with the order ID and transaction details.
Never share passwords, OTPs, payment PINs, or full card security details.

## Cancellation
Cancellation depends on order status. It may be restricted after preparation or delivery
has started. Use the cancellation option in order details if available, or contact support.

## Refunds
Refund eligibility depends on payment status, cancellation reason, and applicable policy.
Processing times depend on the payment provider and bank.
If a refund has not arrived, contact support with the order ID and payment reference.
The AI must not promise a refund before approval.

## Food Complaints
Report missing, incorrect, cold, or damaged food through customer support.
Provide the order ID and a description of the issue.
The support team reviews complaints and determines an appropriate resolution.
Serious food safety concerns must be escalated to a human representative.

## Account Security
Use the official application and available account recovery options.
Never share passwords, OTPs, payment PINs, or sensitive card details.

## Escalation
Escalate to a human when requested, when a payment dispute needs investigation,
when the system cannot answer an order-specific question, or when a serious food
safety concern is reported.

## AI Rules
Answer using the retrieved FAQ context.
Do not invent policies, prices, order statuses, refund timelines, or completed actions.
If the answer is missing, say you do not have enough information and suggest support.
This project has no connection to real orders or payment processing.
`;

// ============================================================
// QUERY CLASSIFICATION
// ============================================================

const QUERY = {
  ORDER_STATUS: "order_status",
  REFUND: "refund",
  GENERAL_QUESTION: "general_question",
  COMPLAINT: "complaint",
};

const classifyPrompt = ChatPromptTemplate.fromMessages([
  [
    "system",
    `Classify the customer message into exactly one category:
     - order_status
     - refund
     - general_question
     - complaint

     Return only the category name.`,
  ],
  ["human", "{message}"],
]);

const classifyChain = classifyPrompt.pipe(llm);

async function findQuery(message) {
  const response = await classifyChain.invoke({ message });

  const category = String(response.content)
    .trim()
    .toLowerCase()
    .replace(/[^a-z_]/g, "");

  return Object.values(QUERY).includes(category)
    ? category
    : QUERY.GENERAL_QUESTION;
}

// ============================================================
// QDRANT INITIALIZATION AND DOCUMENT INGESTION
// ============================================================

let vectorStore;

async function initializeVectorStore() {
  const collections = await qdrantClient.getCollections();

  const exists = collections.collections.some(
    (collection) => collection.name === COLLECTION
  );

  if (!exists) {
    await qdrantClient.createCollection(COLLECTION, {
      vectors: {
        size: 384,
        distance: "Cosine",
      },
    });

    console.log(`Created Qdrant collection: ${COLLECTION}`);
  }

  vectorStore = await QdrantVectorStore.fromExistingCollection(
    embeddings,
    {
      url: QDRANT_URL,
      collectionName: COLLECTION,
    }
  );

  const countResult = await qdrantClient.count(COLLECTION, {
    exact: true,
  });

  // Index the sample FAQ only if this collection is empty.
  if (countResult.count === 0) {
    const splitter = new RecursiveCharacterTextSplitter({
      chunkSize: 800,
      chunkOverlap: 120,
    });

    const chunks = await splitter.splitText(FAQ);

    const documents = chunks.map(
      (pageContent, index) =>
        new Document({
          pageContent,
          metadata: {
            source: "cravio_faq",
            chunk: index + 1,
          },
        })
    );

    await vectorStore.addDocuments(documents);

    console.log(`Indexed ${documents.length} FAQ chunks into Qdrant`);
  } else {
    console.log(`Qdrant already contains ${countResult.count} points`);
  }
}

// ============================================================
// RETRIEVAL
// ============================================================

async function retrieveFAQ(message) {
  const documents = await vectorStore.similaritySearch(message, 4);

  return {
    context: documents
      .map((doc, index) => `[FAQ ${index + 1}]\n${doc.pageContent}`)
      .join("\n\n"),
    sources: documents.map((doc) => ({
      source: doc.metadata?.source || "FAQ",
      chunk: doc.metadata?.chunk ?? null,
      content: doc.pageContent,
    })),
  };
}

// ============================================================
// LANGGRAPH STATE
// ============================================================

const SupportState = Annotation.Root({
  message: Annotation(),
  category: Annotation(),
  context: Annotation(),
  sources: Annotation(),
  answer: Annotation(),
});

// ============================================================
// LANGGRAPH NODES
// ============================================================

async function classifyNode(state) {
  const category = await findQuery(state.message);

  console.log("Detected category:", category);

  return { category };
}

async function retrieveNode(state) {
  const result = await retrieveFAQ(state.message);

  return {
    context: result.context,
    sources: result.sources,
  };
}

async function answerNode(state) {
  const prompt = ChatPromptTemplate.fromMessages([
    [
      "system",
      `You are Cravio's customer support assistant.

       Answer using only the FAQ context below.
       Be polite, concise, and helpful.

       If the answer is not in the context, say you do not have enough
       information and recommend contacting human support.

       Never invent order statuses, policies, prices, refund timelines,
       or completed actions.
       This project cannot access real orders or process refunds.
       Never ask for passwords, OTPs, or payment PINs.

       Customer category: {category}

       FAQ context:
       {context}`,
    ],
    ["human", "{message}"],
  ]);

  const chain = prompt.pipe(llm);

  const response = await chain.invoke({
    category: state.category,
    context: state.context || "No matching FAQ was found.",
    message: state.message,
  });

  return {
    answer: String(response.content),
  };
}

// ============================================================
// BUILD GRAPH
// ============================================================

const graph = new StateGraph(SupportState)
  .addNode("classify", classifyNode)
  .addNode("retrieve", retrieveNode)
  .addNode("generate_answer", answerNode)
  .addEdge(START, "classify")
  .addEdge("classify", "retrieve")
  .addEdge("retrieve", "generate_answer")
  .addEdge("generate_answer", END);

const supportAgent = graph.compile();

// ============================================================
// EXPRESS API
// ============================================================

const app = express();

app.use(express.json({ limit: "1mb" }));

app.get("/health", (req, res) => {
  res.json({
    status: "ok",
    service: "Cravio Customer Support Agent",
  });
});

app.post("/chat", async (req, res) => {
  const message = req.body?.message;

  if (typeof message !== "string" || !message.trim()) {
    return res.status(400).json({
      error: "Please provide a message.",
    });
  }

  try {
    const result = await supportAgent.invoke({
      message: message.trim(),
      category: "",
      context: "",
      sources: [],
      answer: "",
    });

    return res.json({
      question: message.trim(),
      category: result.category,
      answer: result.answer,
      sources: result.sources,
    });
  } catch (error) {
    console.error("Agent error:", error);

    return res.status(500).json({
      error: "Failed to process the question. Check server logs.",
    });
  }
});

// ============================================================
// START SERVER
// ============================================================

async function startServer() {
  await initializeVectorStore();

  app.listen(PORT, () => {
    console.log(`Cravio Support Agent: http://localhost:${PORT}`);
    console.log(`Qdrant dashboard: ${QDRANT_URL}/dashboard`);
  });
}

startServer().catch((error) => {
  console.error("Failed to start application:", error);
  process.exit(1);
});