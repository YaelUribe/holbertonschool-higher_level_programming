#!/usr/bin/node

require('process');

const value = process.argv;
const x = parseInt(value[2]);
function factorial (x) {
  if (isNaN(x) || x === 1 || x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
console.log(factorial(x));
