class Solution(object):
    def canPartition(self, nums):
        if sum(nums)%2 != 0:
            return False
        
        target=(sum(nums)//2)
        dp=[False]*(target+1)
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                if dp[i - num] is True:
                    dp[i] = True
        
        print(dp)
        return dp[target]



        

test=[1,5,11,5]
print(Solution().canPartition(test))
