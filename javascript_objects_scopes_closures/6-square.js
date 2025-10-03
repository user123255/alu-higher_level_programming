#!/usr/bin/node
const Square0 = require('./5-square');

// Defines a class Square that inherits from Square0
class Square extends Square0 {
  charPrint (c) {
    const charToPrint = c || 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(charToPrint.repeat(this.width));
    }
  }
}

module.exports = Square;
