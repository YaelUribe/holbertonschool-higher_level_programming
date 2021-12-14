#!/usr/bin/node

exports.callMeMoby = function (num, functionA) {
  for (let i = 0; i < num; i++) functionA();
};
