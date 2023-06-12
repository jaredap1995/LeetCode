"""
Write a function to find the longest common prefix 
string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

strs=["flower","flow","flight"]
class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if len(prefix) == 0:
                    return ""
        return prefix


    
print(Solution().longestCommonPrefix(strs))

"""This solution works by first checking the length of the list and handling that edge case.
We then set the prefix to teh first string in teh list,
we iterate over the remaining strings in the list and check if the prefix is in the
next string by using the '.find' method.

The key here is that unless the words are identical, in the first iteration of the while loop, 
a -1 will be returned which is not 0, so we enter teh while loop and shorten the 
prefix by one letter.

We continue this process until the prefix returns 0 or we run out of string. """