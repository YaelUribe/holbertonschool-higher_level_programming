#!/usr/bin/node

if (process.argv.length > 3) {
  process.argv.splice(0, 2);
  const maximum = Math.max(...process.argv);
  const nuarray = process.argv.filter(elem => elem !== maximum.toString());
  console.log(Math.max(...nuarray));
} else {
  console.log(0);
}
