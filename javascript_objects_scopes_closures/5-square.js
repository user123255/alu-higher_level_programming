#!/usr/bin/node
const Rectangle = require('./4-rectangle');

// Defines a class Square that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call Rectangle constructor with same value for width & height
  }
}

module.exports = Square;
