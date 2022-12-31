#!/usr/bin/node

const quantity = parseInt(process.argv[2], 10);
if (isNaN(quantity)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${quantity}`);
}
