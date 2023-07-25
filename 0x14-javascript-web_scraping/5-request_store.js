#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
