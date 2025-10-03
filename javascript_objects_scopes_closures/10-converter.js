#!/usr/bin/node
// Function that returns a converter function for a given base
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
