class Solution:
    def wordBreak(s, word_dict):
        n=len(s)
        dp = [False]*(n+1)
        dp[0] = True #Empty string is always segmented

        for i in range(1, n+1):
            for word in word_dict:
                print(dp[i-len(word)])
                if i-len(word)> 0 and dp[i-len(word)] and s[i-len(word):i] == word:
                    dp[i]= True
                    break

        return dp[n]



s = "leetcode"
wordDict = ['leet', 'code']

n=6
dp = [False]*(n+1)
if dp[1-6]:
    print('its a neg')

print(Solution.wordBreak(s, wordDict))