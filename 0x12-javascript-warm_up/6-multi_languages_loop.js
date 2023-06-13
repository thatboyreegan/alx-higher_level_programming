#!/usr/bin/node

import('node:process');

const langauages = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let i = 0;
while (i < langauages.length) {
  console.log(langauages[i]);
  i++;
}
