#!/usr/bin/node
// Script that prints the title of a Star Wars movie by episode number

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
