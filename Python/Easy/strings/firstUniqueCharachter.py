import collections
def solution(s):
    c = collections.Counter(s)
    res = -1
    for i in range(len(s)):
        if c[s[i]] == 1:
            res = i
            break
    
    return res
