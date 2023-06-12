"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only."""

class Solution:
    def lengthOfLastWord(self, s):
        if len(s.split()) == 0: return 0
        return len(s.split()[-1])
    

s = "Hello World     "
print(Solution().lengthOfLastWord(s))


"""Pretty straighforward again. Uses len(s.split)[-1] to retunr length of string."""

    
