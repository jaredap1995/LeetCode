def LIS(nums):
    if not nums:
        return 0
    
    dp = [1]*len(nums)

    for i in range(1, len(nums)):
        for j in range(0,i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j+1])

    return max(dp)

t=[None]*5
c=0
for val in t:
    if val:
        c+=1

print(c)

def solution2(nums):
    if not nums: return 0

    tails = []
    for num in nums:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left+right)//2
            if mid < len(nums) and tails[mid] < num:
                left = mid +1
            else:
                right = mid

        if left >= len(tails):
            tails.append(mid)
        else:
            tails[left] = num

    return len(tails)