# Spolution must use constant space

def allDups(nums):
    res = []
    for x in nums:
        x = abs(x)
        if nums[x-1] < 0:
            res.append(nums)
        nums[x-1] *= -1

    return res