#!/usr/bin/node

const num = Number(process.argv[2]);

if (!num) {
  console.log('Missing size');
} else {
  let strX = '';
  for (let i = 0; i < num; i++) {
    for (let i = 0; i < num; i++) {
      strX += 'X';
    }
    console.log(strX);
    strX = '';
  }
}
