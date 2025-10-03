#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

if (!url) {
  console.log(0);
} else {
  request(url, { json: true }, (err, response, body) => {
    if (err) return console.log(0);

    // SWAPI returns an object with a 'results' array
    if (!body || !body.results) return console.log(0);

    let count = 0;
    body.results.forEach(film => {
      if (film.characters && film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count += 1;
      }
    });
    console.log(count);
  });
}
