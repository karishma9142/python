import "dotenv/config";
import Groq from 'groq-sdk';
import { readpdf } from '../config/readpdf.js';
import { z } from 'zod';

const client = new Groq({
    apiKey: process.env.GROQ_API_KEY
});

const model = 'openai/gpt-oss-120b';


const ExperienceSchema = z.object({
    company: z.string().nullable(),
    role: z.string().nullable(),
    duration: z.string().nullable(),
    description: z.string().nullable(),
    skills_used: z.array(z.string())
});

const ResumeSchema = z.object({
    name: z.string().nullable(),
    email: z.string().nullable(),
    phone: z.string().nullable(),
    total_experience_years: z.number().nullable(),
    skills: z.array(z.string()),
    experiences: z.array(ExperienceSchema),
    education: z.array(z.any()),
    projects: z.array(z.any()),
    certifications: z.array(z.string())
});

const chatRequest = z.object({
    qustion : z.array(z.string)
})

export const askCandidate = async (question, resume) => {

    const systemPrompt = `
You are an AI assistant representing a job candidate.

Below is everything you know about the candidate.

${JSON.stringify(resume, null, 2)}

Rules:

1. Answer only using this information.

2. Never hallucinate.

3. If information is unavailable, say:

"I don't have enough information to answer that."

4. Be professional.

5. Answer as if HR is interviewing this candidate.
`;

    const response = await client.chat.completions.create({

        model: model,

        messages: [
            {
                role: "system",
                content: systemPrompt
            },
            {
                role: "user",
                content: question
            }
        ]
    });

    return response.choices[0].message.content;
};

export const parseResume = async (filePath) => {

    const resumeText = await readpdf(filePath);

    const systemPrompt = `
You are an expert resume parser.

Extract information from the resume based on its meaning,
not only based on exact section headings.

Different resumes may use different headings.

For example:
- Experience
- Professional Experience
- Work History
- Employment
- Internships

These may all contain relevant experience.

Skills may also appear in the skills section, work experience,
internships or projects.

Return ONLY valid JSON.

Important rules:

1. Do not invent information.
2. If a value is not available, return null.
3. If a list has no information, return an empty list.
4. Include internships inside experiences.
5. Extract skills mentioned across the entire resume.

Return JSON in this exact structure:

{
    "name": null,
    "email": null,
    "phone": null,
    "total_experience_years": null,
    "skills": [],
    "experiences": [
        {
            "company": null,
            "role": null,
            "duration": null,
            "description": null,
            "skills_used": []
        }
    ],
    "education": [],
    "projects": [],
    "certifications": []
}
`;

    const userPrompt = `
Parse the following resume:

${resumeText}
`;

    const response = await client.chat.completions.create({
        model,

        messages: [
            {
                role: 'system',
                content: systemPrompt
            },
            {
                role: 'user',
                content: userPrompt
            }
        ],

        response_format: {
            type: 'json_object'
        }
    });

    const rawOutput = response.choices[0].message.content;

    const data = JSON.parse(rawOutput);

    const resume = ResumeSchema.parse(data);

    return resume;
};