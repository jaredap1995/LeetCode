class Solution(object):
    def subset(self, nums):
        result = []
        backtrack([], 0)

        def backtrack(current, start_index):
            result.append(current)
            for i in range(len(nums)-1):
                backtrack(current.append(nums[i], start_index))
        
        return result
