#!/usr/bin/node

const num = parseInt(process.argv.slice(2)[0]);
console.log(num ? 'My number: ' + num : 'Not a number');
