#!/usr/bin/node

import('node:process');

function factorial (x) {
  if (x === 0 || isNaN(x)) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}

const tmp = Number(process.argv[2]);

console.log(factorial(tmp));
