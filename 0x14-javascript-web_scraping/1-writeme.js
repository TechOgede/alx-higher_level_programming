#!/usr/bin/node

const fs = require('fs');
try {
  const content = process.argv[3];
  const path = process.argv[2];
  fs.writeFileSync(path, content, 'utf-8');
} catch (error) {
  console.log(error);
}
