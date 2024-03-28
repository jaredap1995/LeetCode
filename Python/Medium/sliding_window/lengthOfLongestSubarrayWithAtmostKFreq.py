def solution(nums, k):
    hashmap = {}
    length = 0
    left = 0

    for right in range(len(nums)):
        hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1
        if hashmap[nums[right]] > k:
            while nums[left] != nums[right]:
                hashmap[nums[left]] -= 1
                left += 1
            hashmap[nums[left]] -= 1
            left += 1
        length = max(length, right - left + 1)

    return length