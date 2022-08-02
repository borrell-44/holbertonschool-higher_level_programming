#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((h <= 0 || !h) || (w <= 0 || !w)) {
      return;
    } else {
      console.log('%d --- %d', h, w)
      this.width = w;
      this.height = h;
    }
  }
};
