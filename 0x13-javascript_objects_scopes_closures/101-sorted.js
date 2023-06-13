#!/usr/bin/node

const dict = require('./100-data').data;
const newdict = {};

for (const [key, value] of Object.entries(dict)) {
  if (newdict[value] === undefined) {
    newdict[value] = [key];
  } else {
    newdict[value].push(key);
  }
}
console.log(newdict);
