#!/usr/bin/node

import('node:process');

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let tmp = process.argv.slice(2, process.argv.length);
  tmp = tmp.map((value) => Number(value));
  tmp.sort((a, b) => b - a);
  console.log(tmp[1]);
}
