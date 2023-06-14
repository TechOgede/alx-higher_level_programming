#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
