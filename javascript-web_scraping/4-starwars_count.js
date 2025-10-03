#!/usr/bin/node
// Script that prints the number of movies where "Wedge Antilles" is present

const request = require('request');
const url = process.argv[2];
const wedgeId = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(film => {
      if (film.characters.includes(wedgeId)) {
        count++;
      }
    });

    console.log(count);
  }
});
