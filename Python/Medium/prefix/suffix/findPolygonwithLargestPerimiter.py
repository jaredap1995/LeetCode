def solution(nums):
    nums.sort()
    res = 0
    prefix_sum = nums[0]+nums[1]
    for num in nums:
        if prefix_sum > num:
            res = prefix_sum + num
        prefix_sum += num

    return res
