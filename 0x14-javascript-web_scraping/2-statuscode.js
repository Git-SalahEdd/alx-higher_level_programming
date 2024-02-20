#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
