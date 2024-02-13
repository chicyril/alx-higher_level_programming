#!/usr/bin/node

let { argv } = require('process');
argv = argv.slice(2);
if (!argv[0]) console.log('No argument');
else console.log(argv[0]);
