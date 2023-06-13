#!/usr/bin/node

const SquareNew = require('./5-square');

class Square extends SquareNew {
  charPrint (c) {
    if (c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
