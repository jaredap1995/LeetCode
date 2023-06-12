"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]


nums = [2,7,11,15]
target = 9

print(Solution().twoSum(nums,target))


class Solution_hashmap(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for idx, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], idx]
            hashmap[num] = idx


nums = [2,7,11,15]
target = 9

print(Solution_hashmap().twoSum(nums,target))
            

