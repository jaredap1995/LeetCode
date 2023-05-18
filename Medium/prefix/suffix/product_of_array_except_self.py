"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""


class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        
        left, right, output = [0]*length, [0]*length, [0]*length

        left[0] = 1
        for i in range(1, length):
            # Left[i] contains the product of all numbers to the left of element at 'i'.
            left[i] = nums[i - 1] * left[i - 1]

        right[length - 1] = 1
        for i in reversed(range(length - 1)):
            # Right[i] contains the product of all numbers to the right of element at 'i'.
            right[i] = nums[i + 1] * right[i + 1]

        # For the element at index 'i', we find the product of numbers to the left and 
        # the product of numbers to the right.
        for i in range(length):
            output[i] = left[i] * right[i]
        
        return output
    
nums = [1,2,3,4]
print(nums)
print(Solution().productExceptSelf(nums))

