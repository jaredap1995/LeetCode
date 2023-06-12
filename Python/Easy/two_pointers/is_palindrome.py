"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""



class Solution(object):
    def isPalindrome(self, s):
        if s == '': return True
        processed_string=''.join(charachter for charachter in s if charachter.isalnum()).lower()
        return processed_string==processed_string[::-1]
    
    """Uses a list comprehension and string processing to join charachters on spaces if the charachter 
in the string is not an alphanumeric using built in python and then lowercases them.

Compares the original to the new processed result."""


    def two_pointers(self,s):
        i,j=0,len(s)-1
        while i<j:
            while i<j and not s[i].isalnum(): #Just skip over all non-alpha numeric charachters
                i+=1
            while i<j and not s[j].isalnum():
                j-=1

            if s[i].lower() != s[j].lower():
                return False
            
            i +=1
            j -=1

        return True
            


    

s = "A man, a plan, a canal: Panama."
print(Solution().two_pointers(s))




