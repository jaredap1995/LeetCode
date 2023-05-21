"""Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""


nums = [-1,0,1,2,-1,-4]
output=[[-1,-1,2],[-1,0,1]]

class Solution(object):
    def threeSum(self, nums):
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        return output
    
print(Solution().threeSum(nums))


"""This solution uses a set to check for suplicate triplets and a two pointer solution. In order to use two pointers the set must be sorted.
Sort array first then create the set and the resulting output list. Iterate over the array and within the iteration create the two pointers.
This approach is uniqye to the other twoSum problems because the two pointers are initialized within teh loop. This is what I intuitively
tried to do, essentially creating three pointers (the third being the iterator). 


We then go into the two pointer while loop, where j<k we check if the sum is equal to target 0. if it is we add all the numbers to the set and increment both j and k.
If it is greater/less than we appropriately increment j or k and then return to the while loop and try again. If there is no succesful triplety combination
from these three initialized numbers, eventually j will no longer be less tghan k and then we leave while loop and go back to for loop and initialize at a new point in array.

We then turn the set into a list for our answer as teh set effectively prevented from any duplicates."""
