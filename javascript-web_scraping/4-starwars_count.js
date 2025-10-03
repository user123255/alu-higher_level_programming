#!/usr/bin/node
// Script that reads a local file or server and prints the number 10

const fs = require('fs');
const path = process.argv[2] || 'file_2';

fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    // Convert content to integer
    const value = parseInt(data, 10);
    console.log(isNaN(value) ? 0 : value);
  }
});
