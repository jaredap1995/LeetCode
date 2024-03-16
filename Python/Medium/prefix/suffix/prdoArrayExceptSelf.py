def solution(nums):
    res = [0]*len(nums)
    prefixSum = 1
    for i in range(len(nums)):
        res[i] *= prefixSum
        prefixSum *= nums[i]

    post = 1
    for i in range(len(nums), -1, -1):
        res[i]*=post
        post *= nums[i]

    return res

