#!/usr/bin/node

const times = parseInt(process.argv.slice(2)[0]);
if (!times) console.log('Missing number of occurrences');
else for (let i = 0; i < times; i++) console.log('C is fun');
