#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a); // sort descending
  console.log(sorted[1]);
}
