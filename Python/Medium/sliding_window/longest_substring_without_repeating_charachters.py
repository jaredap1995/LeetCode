"""
Given a string s, 
find the length of the longest substring without 
repeating characters.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

s="abcba"

class Solution_incorrect(object):
    def longest_string(self, string):
        start=0
        end=1
        max_length=1
        length=1
        while end < len(string):
            if string[start]==string[end]:
                start=end
                end+=1
                if length>max_length:
                    max_length=length
                    length=1
            else:
                end+=1
                length+=1
        return max_length
    
# print(Solution_incorrect().longest_string(s)) 

s = "abcabcbb"

def lengthOfLongestSubstring(s: str) -> int:
    longest=0
    indexes={}
    offset=0
    for i in range(len(s)):
        char=s[i]
        index=indexes.get(char)
        if index is not None and index >= offset:
            length = i-offset
            offset= index+1
            if length > longest:
                longest=length
        indexes[char]=i

    return max(longest, (len(s)-offset))
    

print(lengthOfLongestSubstring(s))
    



