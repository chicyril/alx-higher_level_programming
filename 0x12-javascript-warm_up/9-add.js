#!/usr/bin/node

const nums = process.argv.slice(2);
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(nums[0]), parseInt(nums[1])));
