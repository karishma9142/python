import fs from 'fs';
import { PDFParse } from 'pdf-parse';

export const readpdf = async (filePath) => {

    const buffer = fs.readFileSync(filePath);

    const parser = new PDFParse({
        data: buffer
    });

    const data = await parser.getText();

    await parser.destroy();

    return data.text;
};