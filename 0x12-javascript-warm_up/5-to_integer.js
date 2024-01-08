#!/usr/bin/node
const { argv } = require('process');
if (!isNaN(argv[2])) { console.log(`My number: ${parseInt(argv[2])}`); } else { console.log('Not a number'); }
