#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  const num = parseInt(process.argv[2]);
  console.log(fac(num));
} else {
  console.log(1);
}

function fac (a) {
  if (a === 1 || a === 0) {
    return 1;
  }
  let num = 1;
  for (let i = a; i > 0; i--) {
    num = num * i;
  }
  return num;
}
