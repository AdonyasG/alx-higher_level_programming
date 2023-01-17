#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const options = {
  url: url,
  method: 'GET'
};
request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
