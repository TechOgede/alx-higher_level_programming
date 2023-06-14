#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  let idx = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    rev[idx++] = list[i];
  }
  return rev;
};
