import { parseResume, askCandidate } from "../services/ai.service.js";
import { z } from "zod";


// Parse Resume
export const parseResumeController = async (req, res) => {

    try {

        if (!req.file) {
            return res.status(400).json({
                success: false,
                message: "Please upload a PDF file"
            });
        }

        const resume = await parseResume(req.file.path);

        return res.status(200).json({
            success: true,
            resume
        });

    } catch (error) {

        console.error(error);

        return res.status(500).json({
            success: false,
            message: "Failed to parse resume"
        });
    }
};


// Ask Candidate
export const askCandidateController = async (req, res) => {
    try {
        const { question } = req.body;

        if (!question) {
            return res.status(400).json({
                success: false,
                message: "Question is required"
            });
        }

        const resume = req.app.locals.resume;

        const answer = await askCandidate(question, resume);

        return res.status(200).json({
            success: true,
            answer
        });

    } catch (error) {
        console.error(error);

        return res.status(500).json({
            success: false,
            message: "Failed to answer question"
        });
    }
};