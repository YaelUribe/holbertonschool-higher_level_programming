#!/usr/bin/node

exports.addMeMaybe = function (number, functionA) {
  functionA(++number);
};
