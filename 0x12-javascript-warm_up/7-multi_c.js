#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  const num = parseInt(process.argv[2]);
  let i = 0;
  for (; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
