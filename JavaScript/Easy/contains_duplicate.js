/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    return (nums.length != new Set(nums).length)
};


nums = [1,2,3,1]
console.log(containsDuplicate(nums))