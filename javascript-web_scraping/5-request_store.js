#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.log('Usage: ./5-request_store.js <URL> <filePath>');
  process.exit(1);
}

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) console.error(err);
  });
});
