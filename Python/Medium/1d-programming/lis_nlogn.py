def ILS(nums):
    if len(nums) == 0 or not nums:
        return 0
    
    # List that stores sorted values in ascending order as they occur in nums.
    # The length of tails is = LIS
    tails = []

# Iterate over arry
    for num in nums:
        left = 0
        right = len(tails)
        # perform binary search
        while left < right:
            mid = (left+right)//2
            if tails[mid] < nums:
                left = mid + 1
            else:
                right = mid

        if len(tails)==left:
            tails.append(num)
        else: 
            tails[left] = num

    return len(tails)
