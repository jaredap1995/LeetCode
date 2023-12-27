from functools import lru_cache

class Solution(object):
    def numDecodings(self, s: str) -> int:
        hashT = {str(num) for num in range(1, 27)}

        @lru_cache(None)
        def dfs(i):
            if i == len(s): return 1
            if s[i] == '0': return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and s[i: i + 2] in hashT:
                res += dfs(i + 2)
            return res
        print(dfs(0))
        return dfs(0)

s='AAJF'
Solution().numDecodings(s)

def solution(s):
    decoder = {str(num) for num in range(1,27)}

    @lru_cache #For memoization
    def dfs(i):
        #If we have reached the length of the string: we can decode it in one way ==> + 1
        if i == len(s): return 1

        # The value at that index is '0', so it is not a value to decode
        if s[i] == '0': return 0

        # Recursively call dfs function on the next charachter
        res = dfs(i+1) 

        # Up to the next charachter is less than length of string and the next two charachters are in decoder (ie '16')
        if i + 1 < len(s) and s[i:i+2] in decoder:
            res += dfs(i+2)

        return res
    
    return dfs(0)
    






















