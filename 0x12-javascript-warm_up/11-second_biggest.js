#!/usr/bin/node
let nums = [];
if (process.argv.lenght <= 3) {
  console.log(0);
}
process.argv.forEach((val, index) => {
  if (index > 1) {
    nums[index - 2] = val;
  }
});

console.log(Math.max(nums));
