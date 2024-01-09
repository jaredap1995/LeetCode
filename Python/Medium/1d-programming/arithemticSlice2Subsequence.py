from collections import Counter
def solution(nums):
    # Similar to the original but due to the subsequence condition we need to modify what we are storing
    # We will use a dp array that is the length of nums which will hold a Counter at each index
    # The value dp[i][j] will actually be dp[i][diff] which is storing the number of subsequences that end at the value i with the common difference of j

    res = 0
    n = len(nums)
    dp = [Counter() for _ in range(n)]

    for i in range(1,n):
        for j in range(i):
            diff = nums[i]-nums[j]

            #Increment the value within teh counter indicating that a subsequence with this difference ends at this value
            dp[i][diff] += 1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                res += dp[j][diff]

    return res