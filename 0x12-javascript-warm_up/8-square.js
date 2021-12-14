#!/usr/bin/node

require('process');

const args = process.argv;
const size = args[2];
let i = 0;
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  while (i < parseInt(args[2])) {
    console.log('X'.repeat(size));
    i++;
  }
}
