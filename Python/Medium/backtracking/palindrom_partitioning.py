class Solution(object):
    def partition(self, s):
        result = []

        def backtrack(start, s, current):
            if start>len(s):
                result.append(tuple(current))
                return
            for j in range(start, len(s)):
                if s[start:j+1]=="".join(reversed(s[start:j+1])):
                    current.append(s[start:j+1])
                    backtrack(j+1, s, current)
                    current.pop()

        backtrack(0, s, [])
        return result
        
