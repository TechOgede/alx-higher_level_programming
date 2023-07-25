#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
const WedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    for (const episode of data.results) {
      if (episode.characters.includes(WedgeAntilles)) {
        count++;
      }
    }
    console.log(count);
  }
});
