"use strict";

function countdown(n) {
  if (n === 0) return null;
  // Creating the base case (if n is 0, return null)
  else console.log(n); // If n is not 0, print n
  countdown(n - 1); // Recursive call for n - 1 (if n is 5 then it will call countdown on n is 4)
}

function doubleCountdown(n) {
  // To print the second countdown I call the previous countdown within it
  countdown(n); // Call the first countdown for n
  countdown(n - 1); // Call it again for n - 1
  console.log(0); // At the end print 0

  return null;
}

doubleCountdown(5);
