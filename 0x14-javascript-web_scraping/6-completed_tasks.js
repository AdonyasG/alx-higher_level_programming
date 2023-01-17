#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body);
    const count = {};
    for (const task of results) {
      if (task.completed === true) {
        if (count[task.userId]) {
          count[task.userId]++;
        } else {
          count[task.userId] = 1;
        }
      }
    }
    console.log(count);
  }
});
