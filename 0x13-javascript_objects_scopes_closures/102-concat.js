const fs = require('fs');

const [, , src1, src2, dest] = process.argv;
const content1 = fs.readFileSync(src1, 'utf-8');
const content2 = fs.readFileSync(src2, 'utf-8');
const concatenatedContent = content1 + content2;
fs.writeFileSync(dest, concatenatedContent, 'utf-8');
