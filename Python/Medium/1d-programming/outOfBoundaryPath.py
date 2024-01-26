def solution(m, n, startRow, startCol, maxMove):
    moves = [(1,0), (0,1), (0,-1), (-1,0)]
    @cache
    def dfs(i,j,moveLeft):
        if i < 0 or i == m or j == n or j < 0: return 1
        if moveLeft == 0: return 0
        ans = 0
        for x, y in moves:
            ans = (ans+dfs(i+x, j+y, moveLeft-1))%(10**9+7)
        return ans
    
    return dfs(startRow, startCol, maxMove)
