#!/usr/bin/node

const list = require('./100-data').list;
const prod = (function () {
  let idx = 0;
  return function (item) {
    return item * idx++;
  };
})();
const newList = list.map(prod);
console.log(list);
console.log(newList);
