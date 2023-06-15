"""
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""

import collections

class Solution(object):
    def characterReplacement(self, s, k):
        if s == "": return 0
        max_len=0
        largest_count=0
        hash_=collections.Counter()
        for idx in range(len(s)):
            hash_[s[idx]]+=1
            largest_count=max(largest_count, hash_[s[idx]])
            if max_len-largest_count>=k:
                hash_[s[idx-max_len]]-=1
            else:
                max_len+=1
        return max_len
    
"""Slightly more readable solution"""
# if s == "": return 0
#         largest_count=0
#         hash_=collections.Counter()
#         left = 0
#         for right in range(len(s)):
#             hash_[s[right]] += 1
#             largest_count = max(largest_count, hash_[s[right]])
#             window_length = right - left + 1
#             if window_length - largest_count > k:
#                 hash_[s[left]] -= 1
#                 left += 1
#         return right - left + 1
    

s = "ADXALBA"
k = 1
print(Solution().characterReplacement(s, k))

