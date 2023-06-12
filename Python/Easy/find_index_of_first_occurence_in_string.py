"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack."""

class Solution:
    def strStr(self, haystack, needle):
        if needle == "": return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        
"""Pretty simple. Checks if needle is an empty string in which case we return 0 because it would
be contained in the other string. Otherwise we use in operatore to check if needle is in haystack,
then return the index of the first occurence of needle in haystack (haystack.index(needle))"""