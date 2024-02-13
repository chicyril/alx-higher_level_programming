#!/usr/bin/node

const num = parseInt(process.argv.slice(2)[0]);
function fact (num) {
  if (!num || num <= 1) return 1;
  return num * fact(num - 1);
}
console.log(fact(num));
