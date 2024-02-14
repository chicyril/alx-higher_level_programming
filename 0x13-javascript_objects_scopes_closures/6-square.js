#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) super.print();
    else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
