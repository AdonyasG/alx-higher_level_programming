#!/usr/bin/node

const quantity = parseInt(process.argv[2], 10);
if (isNaN(quantity)) {
  console.log('Not a number');
} else {
  for (let i = quantity; i > 0; i -= 1) {
    console.log('C is fun');
  }
}
