#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nOccur = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      nOccur++;
    }
  }
  return nOccur;
};
