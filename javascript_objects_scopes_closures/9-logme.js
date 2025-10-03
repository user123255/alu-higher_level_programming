#!/usr/bin/node
// Function that prints the number of arguments already printed and the current argument
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
