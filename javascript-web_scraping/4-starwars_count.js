#!/usr/bin/node
// Script that prints the number of movies where Wedge Antilles (ID 18) is present

const request = require('request');

const url = process.argv[2];
const wedgeId = 'https://swapi-api.alx-tools.com/api/people/18/';

if (!url) {
  console.log(0);
} else {
  request(url, { json: true }, (err, response, body) => {
    if (err) {
      console.log(0);
      return;
    }

    try {
      // body.results contains the list of films
      const films = body.results || [];
      let count = 0;

      for (const film of films) {
        if (film.characters && film.characters.includes(wedgeId)) {
          count++;
        }
      }

      console.log(count);
    } catch (e) {
      console.log(0);
    }
  });
}
