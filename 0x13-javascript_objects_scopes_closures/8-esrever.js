#!/usr/bin/node

exports.esrever = function (list) {
  const reserved = [];
  while (list.length) {
    reserved.push(list.pop());
  }
  return reserved;
};
