def solution(matrix):
    n = len(matrix)

    dp = [[0]*n for _ in range(n)]
    dp[0] = matrix[0]

    for row in range(1,n):
        for col in range(n):
            if col == 0:
                dp[row][col] = matrix[row][col] + min(dp[row-1][col], dp[row-1][col+1])
            elif col == n-1:
                dp[row][col] = matrix[row][col] + min(dp[row-1][col-1], dp[row-1][col])
            else:
                dp[row][col] = matrix[row][col]+ min(dp[row-1][col+1], dp[row-1][col], dp[row-1][col-1])

    
    return min(dp[-1])