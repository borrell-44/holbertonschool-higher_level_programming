#!/usr/bin/node
let num = 0;
process.argv.forEach((val, index) => {
  num = index;
});
if (num === 1) {
  console.log('No argument');
} else if (num === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
