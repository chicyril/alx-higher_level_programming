#!/usr/bin/node

const nums = process.argv.slice(2);
if (nums.length <= 1) {
  console.log(0);
} else {
  const sorted = nums.sort((curr, next) => next - curr);
  console.log(sorted[1]);
}
