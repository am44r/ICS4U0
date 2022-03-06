/*
Given a array of numbers, and a single number n, return an 
extracted array of unique numbers that are 
evenly divisible by n. Your extracted array should be 
sorted in ascending numerical order.
*/

function extractEvenDivisible(arr, n) {
  if (arr.length === 0) return null;
  else {
    if (arr[0] % n !== 0) {
      arr.shift();
      extractEvenDivisible(arr, n);
    }
  }
  return arr;
}

console.log(extractEvenDivisible([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3));
