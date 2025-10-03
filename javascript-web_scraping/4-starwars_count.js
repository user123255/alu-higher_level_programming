#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const pathOrUrl = process.argv[2];

if (!pathOrUrl) {
  console.log(0);
} else if (pathOrUrl.startsWith('http://') || pathOrUrl.startsWith('https://')) {
  // Use request for URLs
  request(pathOrUrl, { json: true }, (err, response, body) => {
    if (err) return console.log(0);
    // Assuming the body is an array or object with array
    console.log(body.length || 0);
  });
} else {
  // Use fs for local files
  fs.readFile(pathOrUrl, 'utf-8', (err, data) => {
    if (err) return console.log(0);
    const lines = data.split('\n').filter(Boolean);
    console.log(lines.length);
  });
}
