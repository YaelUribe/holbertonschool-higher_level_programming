#!/usr/bin/node

exports.converter = function (base) {
  function myConverter (stuff) {
    return Number.toString(base);
  }
  return myConverter;
};
