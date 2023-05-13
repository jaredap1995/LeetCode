"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k."""

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
nums=[3,2,2,3]
val=3
print(Solution().removeElement(nums,val))

"""Solution works because when i=0 at start, unles nums is empty, condition will always be true.
We move forward through loop and if nums[i] is equal to val, we remove it from nums.
othwerise we know that index of nums should be included and then we increment i instead."""


class Solution:
    def removeEelement(self, nums, val):
        i,j=0,0
        while j <len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
    

nums=[7,7,9,9,10,7]
val=7
print(Solution().removeEelement(nums,val))

"""Solution uses two pointer approach which is more computationally efficient than approach where we pop.
This approach works because we use j to iterate over list and i to keep track of the number of values that do not equal val.
We iterate through list and if nums[j] is equal to val we move on, if it is not equal to val,
we set nums[i] equal to nums[j] (number of values equal to place in iteration) and increment number of values."""