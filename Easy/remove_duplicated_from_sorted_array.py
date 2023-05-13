"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
        return i+1
    
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))

"""Two pointer Solution. First checks if the array is empty,
if the array is empty then there are no duplicates and the length is zero.
We initialize the first pointer which is i=0, it indicates the first element of the array.
We then begin a second pointer j=1 which is the second element of the array.
Inside the loop we iterate through the array, first checking if nums[i] is equal to nums[j],
if it is then we skip, if it is not then we know that nums j is not a duplicate,
therefore we increment i (the number of unique values) by 1 and set the next element of the array,
nums[i+1] equal to nums[j]"""
