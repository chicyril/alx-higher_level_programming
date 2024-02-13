#!/usr/bin/node

exports.addMeMaybe = (number, theFunction) => {
  number++;
  theFunction(number);
};
