#!/usr/bin/node

import('node:process');

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
