#!/usr/bin/node

exports.convert = function (base) {
  return value => value.toString(base);
};
