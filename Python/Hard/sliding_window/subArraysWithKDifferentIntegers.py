"""
General Approach to all of the subarray sliding window problems

for right in range(len(arr)):
    do_something(nums[right]) ==> Could be (res +=, prod *=, hashmap[nums[right]] += 1, if nums[right] == val etc.)
    while(!condition(nums[left])):
        do_something_by_removing(nums[left])
        left ++
    update_answer

"""
class Solution:
    def s(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k-1)
    
    def atMost(self, nums, k):
        hashmap = {}
        left = 0
        res = 0

        for right in range(len(nums)):
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1
            while len(hashmap) > k:
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    hashmap.pop(nums[left])
                left +=1 
            res += right - left + 1
        
        return res

