#!/usr/bin/node
const fs = require('fs');
const listFiles = process.argv.slice(2);
let content = '';
for (let i = 0; i < listFiles.length - 1; i++) {
  content += fs.readFileSync(listFiles[i], 'utf8');
}

fs.writeFileSync(listFiles[listFiles.length - 1], content);
