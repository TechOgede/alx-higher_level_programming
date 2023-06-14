#!/usr/bin/node

exports.logMe = (function () {
  let num = 0;
  return function (item) {
    console.log(`${num}: ${item}`);
    ++num;
  };
})();
