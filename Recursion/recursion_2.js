/*
Given a array of numbers, and a single number n, return an 
extracted array of unique numbers that are 
evenly divisible by n. Your extracted array should be 
sorted in ascending numerical order.
*/

const extractEvenlyDivisible = (numbers, n) => {
  if (numbers.length === 0) return [];
  if (numbers[0] % n !== 0) return extractEvenlyDivisible(numbers.slice(1), n);
  return [numbers[0]].concat(extractEvenlyDivisible(numbers.slice(1), n));
}

final_array = [...new Set(extractEvenlyDivisible([1,9,3,4,3,6,7,8,9], 3).sort())];
console.log(final_array);




// Testing the slice() function
// let arr = [1, 2, 3];
// arr = arr.slice(1);
// console.log(arr);

// Learning spread syntax + set to sort array and remove repeated values.
// let arr = [3, 1, 3, 2, 3, 4];
// mod_arr = [...new Set(arr)];
