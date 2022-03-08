/*
Given a array of numbers, and a single number n, return an 
extracted array of unique numbers that are 
evenly divisible by n recursivley. Your extracted array should be 
sorted in ascending numerical order.
*/

function extractEvenDivisible(numbers, n) {
  if (numbers.length === 0) return [];
  if (numbers[0] % n !== 0) return extractEvenDivisible(numbers.slice(1), n);
  return [numbers[0]].concat(extractEvenDivisible(numbers.slice(1), n));
}

console.log(extractEvenDivisible([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3));
