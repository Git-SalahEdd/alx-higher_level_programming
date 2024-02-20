#!/usr/bin/node

const args = process.argv;
const request = require('request');

const fs = require('fs');

request(args[2], (err, code, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(args[3], body, 'utf-8', (err) => {
      if (err) { console.error(err); }
    });
  }
});
