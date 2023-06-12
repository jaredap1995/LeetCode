"""Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 

If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""


nums = [-1,0,3,5,9,12]
target = 9

# sol = [idx for idx,i in enumerate(nums) if target==i]

class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                right-=1
            if nums[mid]<target:
                left+=1
        return -1



print(Solution().search(nums,target))

