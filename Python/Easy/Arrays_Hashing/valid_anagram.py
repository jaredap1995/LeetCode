"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

s = "aa"
t = "a"

print(Solution().isAnagram(s,t))

"Uses native sorted method to orgainze the values in a set."