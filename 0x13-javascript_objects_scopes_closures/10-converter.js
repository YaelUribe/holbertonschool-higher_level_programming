#!/usr/bin/node

exports.converter = function (base) {
  function converter (stuff) {
    return stuff.toString(base);
  }
  return converter;
};
