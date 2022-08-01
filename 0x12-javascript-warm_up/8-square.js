#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  const num = parseInt(process.argv[2]);
  let out = '';
  for (let i = 1; i <= num; i++) {
    for (let y = 0; y < num; y++) {
      out += 'X';
    }
    if (i !== num) {
      out += '\n';
    }
  }
  if (out !== '') {
    console.log(out);
  }
} else {
  console.log('Missing size');
}
