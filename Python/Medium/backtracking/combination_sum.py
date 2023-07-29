class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current_sum, current):
            if current_sum > target:
                return
            elif current_sum == target:
                result.append(current.copy())
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])

                backtrack(start, current_sum+candidates[i], current)

                current.pop()

        backtrack(0,0,[])
        return result 
