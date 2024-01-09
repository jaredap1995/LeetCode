def solution(nums):
    n = len(nums)
    res = 0
    temp = 0

    for i in range(2, n):
        diff = nums[i]-nums[i-1]
        diff2 = nums[i-1]-nums[i-2]

        if diff == diff2:
            temp +=1
            #Use a temporary value that will keep track of subarrays as potential length increases
            res += temp

        else:
            temp = 0

    return res

