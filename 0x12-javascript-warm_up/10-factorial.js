#!/usr/bin/node

function factorial (num) {
  if (!num) {
    return (1);
  }
  return (num * factorial(num - 1));
}

const num = Number(process.argv[2]);
console.log(factorial(num));
