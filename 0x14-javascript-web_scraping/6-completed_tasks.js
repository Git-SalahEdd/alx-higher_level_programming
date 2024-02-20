#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (err, code, body) => {
  if (err) { console.error(err); } else {
    const users = {};
    for (const element in JSON.parse(body)) {
      if (JSON.parse(body)[element].completed) {
        users[JSON.parse(body)[element].userId] = (users[JSON.parse(body)[element].userId] || 0) + 1;
      }
    }
    console.log(users);
  }
});
