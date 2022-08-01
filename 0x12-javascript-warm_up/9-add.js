#!/usr/bin/node
if (!isNaN(process.argv[2]) || !isNaN(process.argv[3])) {
  const num1 = parseInt(process.argv[2]);
  const num2 = parseInt(process.argv[3]);
  console.log(add(num1, num2));
} else {
  console.log(NaN);
}

function add (a, b) {
  return a + b;
}
