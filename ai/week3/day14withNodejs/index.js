import { CharacterTextSplitter } from "@langchain/textsplitters";

const document = `
# Introduction to React

React is a JavaScript library used for building user interfaces. It was developed by Facebook and is now maintained by Meta and the open-source community.

## Components

React applications are built using components. A component is a reusable piece of UI that can contain its own logic and structure. Components make large applications easier to develop and maintain.

## Props

Props are used to pass data from one component to another. They are read-only and help components communicate with each other.

## State

State is used to store data that can change over time. When the state of a component changes, React can update the user interface automatically.

## Conclusion

React makes it easier to build interactive and reusable user interfaces. Components, props, and state are some of the most important concepts to understand when learning React.
`;

// 1. Fixed-Size Chunking

const splitter = new CharacterTextSplitter({
    chunkSize : 100,
    chunkOverlap : 10
});

const chunks = await splitter.splitText(document);
console.log("Fixed Size Chunks:", chunks.length);
console.log(chunks[0]);