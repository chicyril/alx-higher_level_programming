#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((occur, num) => (num === searchElement
    ? occur + 1
    : occur), 0);
};
