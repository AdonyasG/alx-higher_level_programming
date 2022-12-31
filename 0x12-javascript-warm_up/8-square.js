#!/usr/bin/node

const quantity = parseInt(process.argv[2], 10);
if (isNaN(quantity)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < quantity; i += 1) {
    console.log('X'.repeat(quantity));
  }
}
