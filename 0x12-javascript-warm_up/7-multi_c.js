#!/usr/bin/node

import('node:process');

const tmp = Number(process.argv[2]);
let i = 0;

if (isNaN(tmp)) {
  console.log('Missing number of occurrences');
} else {
  while (i < tmp) {
    console.log('C is fun');
    i++;
  }
}
