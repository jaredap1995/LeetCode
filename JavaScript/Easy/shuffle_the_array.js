//Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

//Return the array in the form [x1,y1,x2,y2,...,xn,yn].


/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let solved =[]
    for (let i of Array(n).keys()){
        solved.push(nums[i])
        solved.push(nums[n+i])
    }
    return solved
};