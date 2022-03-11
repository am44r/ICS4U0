/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = function(nums) {
    return[...new Set([nums])];
    
};

console.log(removeDuplicates)