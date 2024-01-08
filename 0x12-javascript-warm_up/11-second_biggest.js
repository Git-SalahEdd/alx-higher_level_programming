#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 3) { console.log('0'); } else {
  const arr = argv.slice(2);
  arr.sort((x, y) => (parseInt(y) - parseInt(x)));
  console.log(arr[1]);
}
