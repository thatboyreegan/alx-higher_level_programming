#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w && w > 0) && (h && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  doubles () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
