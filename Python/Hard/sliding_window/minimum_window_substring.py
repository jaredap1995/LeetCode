"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
of s such that every character in t (including duplicates) is included in the window. 

If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

"""


import collections

class Solution(object):
    def minWindow(self, s, t):
        if s==t: return s
        left, right=0, 0
        start,end=0,0

        min_window_size=float('inf') #Needs to be large number

        need=len(t) #Needful charachter count: Counter indicating how many charachters we still need
        #to get a valid window that contains all charachters 't'

        window=collections.Counter() #Counts the number of valid charachters in the window
        counter_t=collections.Counter(t) #Counter of t charachters

        while right<len(s):
            window[s[right]]+=1
            if s[right] in t:
                if window[s[right]]<=counter_t[s[right]]:
                    need-=1 
            right+=1
            while need ==0:
                if right - left < min_window_size: #Meaning we have found a smaller window
                    start, end = left, right #We update the indexes of the window
                    min_window_size=right-left # Update min_window_size
                if s[left] in counter_t:
                    window[s[left]]-=1
                    if window[s[left]]<counter_t[s[left]]:
                        need+=1
                left+=1
        if min_window_size==float('inf'): 
            return ""
        else:
            return s[start:end]
            


s = "bbaa"
t = "aba"

print(Solution().minWindow(s, t))

