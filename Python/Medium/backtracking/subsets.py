class Solution(object):
    def subsets(self, nums):
        result = []
        
        def backtrack(i, current):
            if i >=len(nums):
                result.append(current.copy())
                return
            current.append(nums[i])
            backtrack(i+1, current)

            current.pop()
            backtrack(i+1, current)
        backtrack(0, [])
        return result