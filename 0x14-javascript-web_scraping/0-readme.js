#!/usr/bin/node
const fs = require('fs');

try {
  const content = fs.readFileSync(process.argv[2], 'utf-8');
  console.log(content);
} catch (error) {
  console.log(error);
}
