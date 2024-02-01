def solution(nums, k):
    size = 3
    nums.sort()
    res = []

    def helper(arr):
        diffs = []
        for i in range(1,len(arr)):
            diffs.append(arr[i]-arr[i-1])
        diffs.append(arr[2]-arr[0])
        return diffs
    
    for i in range(0, len(nums), size):
        mini = nums[i:i+size]
        if any(isinstance(diff, int) and diff > k for diff in helper(mini)):
            return []
        res.append(mini)

    return res
