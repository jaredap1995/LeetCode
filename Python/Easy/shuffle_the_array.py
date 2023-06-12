"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

"""


nums = [2,5,1,3,4,7] 
n = 3

output=[2,3,5,4,1,7]

class Solution(object):
    def shuffle(self, nums, n):
        solved=[]
        low=0
        for i in range(len(nums)):
            solved.append(nums[low])
            solved.append(nums[n])
            low+=1
            n+=1
            if n>=len(nums):
                return solved
        return solved





print(Solution().shuffle(nums, n))
