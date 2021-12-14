#!/usr/bin/node

require('process');

const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
add(a, b);
