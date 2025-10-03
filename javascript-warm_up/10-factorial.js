#!/usr/bin/node

function factorial (n) {
  const num = parseInt(n);
  if (isNaN(num) || num <= 1) return 1;
  return num * factorial(num - 1);
}

const args = process.argv.slice(2);
console.log(factorial(args[0]));
