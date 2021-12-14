#!/usr/bin/node

exports.converter = function (base) {
  function converter (stuff) {
    return Number.toString(base);
  }
  return converter;
};
