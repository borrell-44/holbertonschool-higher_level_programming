#!/usr/bin/node

const list = require('./100-data').list;
const ar = list.map((i, y) => i * y);
console.log(list);
console.log(ar);
