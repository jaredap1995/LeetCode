"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""
import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        counter, window = collections.Counter(s1), len(s1)
        for i in range (len(s2)):
            if s2[i] in counter:
               counter[s2[i]]-=1
            if i>=window and s2[i-window] in counter:
                counter[s2[i-window]]+=1

            if all([counter[i]==0 for i in counter]): 
                return True
            
        return False

            

s1 = "ab"
s2 = "eidboaoo"