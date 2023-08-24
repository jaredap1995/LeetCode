class Solution:
    def longestPalindrome(s):
        longest = ''
        dp_table=[[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp_table[i][i]=True
            longest=s[i]

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i]==s[j]:
                    if j-i == 1 or dp_table[i+1][j-1] is True:
                        dp_table[i][j] = True
                        if len(longest)<len(s[i:j+1]):
                            longest=s[i:j+1]

        return dp_table, longest
    

s="ababc"
print(Solution.longestPalindrome(s))