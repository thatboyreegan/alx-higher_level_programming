#!/usr/bin/node

import('node:process');

let tmp = Number(process.argv[2]);

if (isNaN(tmp)) {
  console.log('Not a number');
} else {
  tmp = parseInt(process.argv[2]);
  console.log(`My number: ${tmp}`);
}
