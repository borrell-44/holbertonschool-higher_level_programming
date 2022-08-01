#!/usr/bin/node
let num = 0;
process.argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
  }
  num = index;
});
if (num === 1) {
  console.log('No argument');
}
