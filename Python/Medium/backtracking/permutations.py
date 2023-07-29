class Solution:
    def permute(self, nums):
        result = []
        visited = set()

        def backtrack(result, visited, subset, nums):
            if len(subset) == len(nums):
                result.append(subset.copy())

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtrack(result, visited, subset+[nums[i]], nums)
                    visited.remove(i)
        backtrack(result, visited, [], nums)
        return result

