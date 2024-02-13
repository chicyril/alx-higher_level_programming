#!/usr/bin/node

const size = parseInt(process.argv.slice(2)[0]);
if (!size) console.log('Missing size');
else for (let i = 0; i < size; i++) console.log('X'.repeat(size));
