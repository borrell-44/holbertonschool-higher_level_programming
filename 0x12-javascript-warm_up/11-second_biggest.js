#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const ar = process.argv.slice(2);
  if (ar.length > 2) {
    const index = ar.indexOf(Math.max.apply(null, ar));
    ar.splice(index, 1);
  }
  console.log(Math.max.apply(null, ar));
}
