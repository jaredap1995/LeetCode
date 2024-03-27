def solution(nums, k):
    if k <= 1:
        return 0
    
    prod = 1
    n = len(nums)
    left = 0
    count = 0


    for i in range(n):
        prod *= nums[i]

        while prod >= k:
            prod //= nums[left]
            left += 1
        
        count += i - left + 1

    return count
    