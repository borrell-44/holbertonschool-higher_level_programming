#!/usr/bin/node

const addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
exports.addMeMaybe = addMeMaybe;
