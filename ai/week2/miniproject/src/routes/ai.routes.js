import express from "express";

import {
    parseResumeController,
    askCandidateController
} from "../controller/ai.controller.js";

const router = express.Router();

router.post(
    "/parse-resume",
    parseResumeController
);

router.post(
    "/ask",
    askCandidateController
);

export default router;