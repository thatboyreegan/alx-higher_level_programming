#!/usr/bin/node

import('node:process');

const tmp = Number(process.argv[2]);
let j = 0;

if (isNaN(tmp)) {
  console.log('Missing size');
} else {
  let size = '';
  while (j < tmp) {
    size += 'X';
    j++;
  }
  j = 0;
  while (j < tmp) {
    console.log(size);
    j++;
  }
}
