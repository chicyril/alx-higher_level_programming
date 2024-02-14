#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  constructor (size) {
    super(size, size);
    this.size = this.width;
  }

  charPrint (c) {
    if (!c) super.print();
    else {
      for (let i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
