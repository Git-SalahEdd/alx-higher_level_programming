#!/usr/bin/node
const { argv } = require('process');
let row;
if (!isNaN(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    row = '';
    for (let j = 0; j < parseInt(argv[2]); j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
