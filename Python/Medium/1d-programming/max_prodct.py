class Solution(object):
    def maxProduct(self, nums):
        ans = maxp = minp = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], maxp*nums[i], minp*nums[i])
            minp=min(nums[i], maxp*nums[i], minp*nums[i])
            maxp=temp
            ans=max(maxp,ans)

        return ans

nums = [2,3,4]
print(Solution().maxProduct(nums=nums))