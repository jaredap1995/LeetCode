"""Running Sum of 1D Array

Given an array nums, return an array such that, for each element at index i in the original array, 
the new value is the sum of all numbers in the original array up to and including i.

Example:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""


class Solution:
    def runningSum(self, nums):
        output=[0]*len(nums)
        output[0]=nums[0]
        for i in range(1, len(nums)):
            output[i]=nums[i]+output[i-1]
        return output
    
nums=[1,2,3,4]
print(Solution().runningSum(nums))