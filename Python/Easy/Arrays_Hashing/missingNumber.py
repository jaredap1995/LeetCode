def solution(nums):
    nums.sort()
    res = -1
    n = len(nums)
    for i in range(len(nums)):
        if i != nums[i]:
            res = i
            break
    
    return res if res != -1 else n
