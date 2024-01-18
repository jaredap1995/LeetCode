def solution(n):
    if n==1:return 1
    if n == 2: return 2

    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(1,n+1):
        if dp[i] == 0:
            dp[i] = dp[i-2]+dp[i-1]

    return dp[n]
