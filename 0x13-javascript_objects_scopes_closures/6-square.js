#!/usr/bin/node

const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let str = '';
      for (let i = 0; i < this.height; i++) {
        for (let i = 0; i < this.width; i++) {
          str += c;
        }
        console.log(str);
        str = '';
      }
    }
  }
};
