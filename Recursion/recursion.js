/**
 * @name recursion_1
 * @author Amaar Sana
 * @description Given a non-negative integer n, create a double 
                countdown-pattern in the console.

 * @studentNumber 917364
 */

/**
 *
 * @param {Number} n
 * @param {Number} [counter]
 */

// Using counter default parameter
const doubleCountdown = (n, counter = 0) => {
  // Base case; checks if (n) = counter
  // If true returns 0
  if (n === counter) return 0;
  // If base case not true log (n - counter) to console
  console.log(n - counter);
  // Call the function recursively, passing (n) and incremented counter
  doubleCountdown(n, counter + 1);
  console.log(counter);
  return 1;
};

// Test Cases
doubleCountdown(5);
doubleCountdown(6);
doubleCountdown(3);

// Test cases for you to create
//doubleCountdown(n)
//doubleCountdown(n)
//doubleCountdown(n)
