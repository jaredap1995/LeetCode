class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        if len(nums) == 3: return max(nums[0], nums[2], nums[1])

        n=len(nums)
        robbed_1=[0]*(n-1)
        robbed_1[0], robbed_1[1]=nums[0], max(nums[0], nums[1])
        print(robbed_1)

        robbed_2=[0]*(n-1)
        robbed_2[0], robbed_2[1]=nums[1], max(nums[0], nums[1])
        print(robbed_2)

        for i in range(2, n-1):
            robbed_1[i]=max(robbed_1[i-2]+nums[i], robbed_1[i-1])
        for i in range(2, n-1):
            robbed_2[i]=max(robbed_2[i-2]+nums[i+1], robbed_2[i-1])

        print(robbed_1, robbed_2)
        return max(robbed_1[-1], robbed_2[-1])
    
nums=[1,2,3,1]
print(Solution().rob(nums))