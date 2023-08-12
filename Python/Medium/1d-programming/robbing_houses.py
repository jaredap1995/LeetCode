class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1: return nums[0]
        if len(nums)==2: return max(nums[0], nums[1])
        if len(nums)==3: return max(nums[0]+nums[2], nums[1])

        robbed=[0]*len(nums)#Will hold max value I can rob up to nums[i]
        robbed[0]=nums[0]
        robbed[1]=max(robbed[0], robbed[1])
        n=len(nums)

        for i in range(2, n):
            # If rob or not robbing assessed by robbing current house or not
            robbed[i] = max(robbed[i-2]+nums[i], robbed[i-1])
        print(robbed)
        return robbed[-1]

    

nums=[1,2,1,1]
print(Solution().rob(nums))