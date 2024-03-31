def solution(nums, minK, maxK):
    minl = -1
    maxl = -1
    res = 0
    left = 0

    for right in range(len(nums)):
        val = nums[right]
        if val < minK or val > maxK:
            minl = -1
            maxl = -1
            left = right + 1
        else:
            if val == minK:
                minl = right
            if val == maxK:
                maxl = right
            res += max(0, min(minl, maxl) - left + 1)

    return res
