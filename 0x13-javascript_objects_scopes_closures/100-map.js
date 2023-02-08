#!/usr/bin/node
// Script that imports an array and computes a new array.

const list = require('./100-data').list;

const newlist = list.map((v, k) => v * k);
console.log(list);
console.log(newlist);
