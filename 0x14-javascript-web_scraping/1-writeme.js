#!/usr/bin/node
const fs = require('fs');
const args = process.argv[2];
const content = process.argv[3];
fs.writeFile(args, content, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  // file written
});
