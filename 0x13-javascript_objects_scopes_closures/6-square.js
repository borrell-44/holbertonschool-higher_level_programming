#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let pr = 'C';
    if (!c) {
      pr = 'X';
    }

    let ch = '';
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        ch += pr;
      }
      if (i !== this.height) {
        ch += '\n';
      }
    }
    console.log(ch);
  }
};
