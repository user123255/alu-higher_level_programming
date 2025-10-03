#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0]);

if (!num && num !== 0) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
