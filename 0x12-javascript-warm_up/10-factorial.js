#!/usr/bin/node

function fac (num) {
  if (num <= 1) {
    return 1;
  }
  return num * (fac(num - 1));
}

if (process.argv.length <= 2) {
  console.log(1);
} else if (!isNaN(process.argv[2])) {
  const num = parseInt(process.argv[2]);
  console.log(fac(num));
} else {
  console.log(1);
}
