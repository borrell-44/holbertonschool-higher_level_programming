#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((h <= 0 || !h) || (w <= 0 || !w)) {
      // pass
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let pr = '';
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        pr += 'X';
      }
      if (i !== this.height) {
        pr += '\n';
      }
    }
    console.log(pr);
  }

  rotate () {
    const he = this.height;
    this.height = this.width;
    this.width = he;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
