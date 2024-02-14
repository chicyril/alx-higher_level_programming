#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (const el of list) reversed.unshift(el);
  return reversed;
//   return list.toReversed();
};
