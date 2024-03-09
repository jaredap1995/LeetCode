def solution(grid, k):
    res = 0
    m= len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            this = grid[i][j]
            if i > 0:
                this += dp[i-1][j]
            if j > 0:
                this += dp[i][j-1]
            if i > 0 and j > 0:
                this -= dp[i-1][j-1]

            dp[i][j] = this
            if this <=k:
                res += 1 
    
    return res