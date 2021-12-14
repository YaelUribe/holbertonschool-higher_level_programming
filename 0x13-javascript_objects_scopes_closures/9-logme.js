#!/usr/bin/node

let x = 0;
exports.logMe = function (stuff) {
  console.log(`${x}: ${stuff}`);
  x++;
};
