#!/usr/bin/node

require('process');

const args = process.argv;
let i = 0;
if (isNaN(args[2])) {
  console.log('Missing number of ocurrences');
} else {
  while (i < parseInt(args[2])) {
    console.log('C is fun');
    i++;
  }
}
