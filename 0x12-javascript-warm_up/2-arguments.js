#!/usr/bin/node

const len = process.argv.length - 2;

if (!len) {
  console.log('No argument');
} else if (len === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
