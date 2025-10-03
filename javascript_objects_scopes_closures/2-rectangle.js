#!/usr/bin/node
// Defines a class Rectangle with width and height
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    // else do nothing → creates an empty object
  }
}

module.exports = Rectangle;
