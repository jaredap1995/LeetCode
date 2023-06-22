"""
Given an array of integers nums containing n + 1 integers 
where each integer is in the range [1, n] inclusive.

^^^
This is the important giveaway regardining the pigeonhole theory, each integer in the
array is [1,n] (lets say n=5) so each number is in range [1,5] and you have an array
of n+1 numbers (meaning 5+1). So we have 6 numbers, but every number is in range [1,5].
This means there must be at least one duplicate.

Same thing applies on weird test cases like [2,2,2,2,2]. Here the range is [1,4],
so all values fall within that range and the array is 5 values long. Despite multiple
of two, it is still valid.


There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only 
constant extra space.

"""


nums = [1,3,4,2,2]


class Solution(object):
    def findDuplicate(self, nums):
        slow=nums[0]
        fast=nums[0]

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break

        slow=nums[0]

        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return slow