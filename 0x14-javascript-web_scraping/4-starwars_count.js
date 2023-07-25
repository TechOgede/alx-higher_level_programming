#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    for (const episode of data.results) {
      for (const character of episode.characters) {
        if (character.search('18') > 0) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
