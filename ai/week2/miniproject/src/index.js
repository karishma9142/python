import express from "express";
import aiRoutes from "./routes/ai.routes.js";
import { parseResume } from "./services/ai.service.js";

const app = express();

app.use(express.json());

let resume;

const startServer = async () => {
    resume = await parseResume("./src/services/resume/resume.pdf");

    app.locals.resume = resume;

    app.use("/api/ai", aiRoutes);

    app.listen(3000, () => {
        console.log("Server running on port 3000");
    });
};

startServer();