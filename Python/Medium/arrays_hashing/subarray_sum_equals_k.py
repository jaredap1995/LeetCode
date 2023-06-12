"""
Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of 
elements within an array.

"""

#Size of window can in theory be all the way 
# up to the size of the array
class Solution(object):
    def subarraySum(self, nums, k):
        sum_dict={0:1}
        cum_sum=0
        count=0
        for i in range(len(nums)):
            cum_sum+=nums[i]
            if cum_sum - k in sum_dict:
                count+=sum_dict[cum_sum-k]
            if cum_sum in sum_dict:
                sum_dict[cum_sum]+=1
            else: 
                sum_dict[cum_sum]=1
        return count