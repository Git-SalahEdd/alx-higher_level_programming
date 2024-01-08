#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('1');
} else {
  console.log(myFactorial(parseInt(argv[2])));
}

function myFactorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } return (n * myFactorial(n - 1));
}
