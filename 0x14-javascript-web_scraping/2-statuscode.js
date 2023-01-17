#!/usr/bin/node
const http = require('https');
const url = process.argv[2];

http.get(url, (res) => {
  console.log('code: ' + res.statusCode);
}).on('error', function (err) {
  console.error(err);
});
