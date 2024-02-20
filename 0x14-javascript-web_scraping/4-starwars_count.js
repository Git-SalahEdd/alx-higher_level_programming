#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (err, code, body) => {
  if (err) {
    console.error(err);
  } else {
    let n = 0;
    for (const film in JSON.parse(body).results) {
      for (const character in JSON.parse(body).results[film].characters) {
        if (JSON.parse(body).results[film].characters[character].includes('18')) { n += 1; }
      }
    }
    console.log(n);
  }
});
