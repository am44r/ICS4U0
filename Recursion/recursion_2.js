/**
 * @name recursion_2
 * @author Amaar Sana
 * @description Given a array of numbers, and a single number n, return an 
                extracted array of unique numbers that are 
                evenly divisible by n. Your extracted array should be 
                sorted in ascending numerical order.
 * @studentNumber 917364
 */

/**
 *
 * @param {array} numbers
 * @param {Number} n
 * @returns {array} - Array of the numbers divisible by (n)
 */

const extractEvenlyDivisible = (numbers, n) => {
  // Base case (checks if the array is empty or (n) = 0 becuase nothing is divisble by 0)
  if (numbers.length === 0 || n === 0) return [];
  // Checks if the first index of the array is NOT divisible by (n). If it isn't, we slice off that index and return the function
  if (numbers[0] % n !== 0) return extractEvenlyDivisible(numbers.slice(1), n);
  return [
    // Creates a collection where a value may only appear once
    ...new Set(
      [numbers[0]]
        // Conactinating two arrays together (Divisible Value + the left over array after slicing off the first value)
        .concat(extractEvenlyDivisible(numbers.slice(1), n))
        // Compare function using .sort() method
        // Compares two values in the array (a, b)
        // If result is negative, (a) is sorted before (b) - a<b
        .sort((a, b) => {
          // Returns the result (neg) or (pos)
          return a - b;
        })
    ),
  ];
};

// 3 Test cases
console.log(extractEvenlyDivisible([1, 9, 3, 4, 3, 6, 7, 8, 9], 3));
console.log(extractEvenlyDivisible([1, 5, 6, 3, 2, 6, 54, 23, 23, 12], 2));
console.log(extractEvenlyDivisible([43, 42, 2, 12, 23, 12, 34, 5], 6));

// Test cases for you to create
//console.log([], n)
//console.log([], n)
//console.log([], n)
