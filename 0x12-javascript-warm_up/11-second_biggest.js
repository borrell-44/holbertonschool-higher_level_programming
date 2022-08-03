#!/usr/bin/node
if (process.argv.length <= 3) {
    console.log(0);
}
else {
    const ar = process.argv.slice(2);
    ar.sort();
    console.log(parseInt(ar[ar.length - 2]));
}
