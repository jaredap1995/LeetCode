"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set). 
"""

def subsets2(self, nums):
    result = []
    nums.sort()

    def backtrack(index, current):
        if index>=len(nums):
            if current not in nums:
                result.append(current.copy())
                return
            else:
                return
        current.append(nums[index])
        backtrack(index+1, current)

        current.pop()
        backtrack(index+1, current)
    backtrack(0,[])
    return result




