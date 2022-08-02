#!/usr/bin/node

exports.esrever = function (list) {
  const hold = [];
  let cur = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    hold[cur] = list[i];
    cur += 1;
  }
  return hold;
};
