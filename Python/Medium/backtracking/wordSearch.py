def solution(board, word):
    n = len(board)
    m = len(board[0])

    def backtrack(i,j,suffix):
        if len(suffix) == 0:
            return True

        if (i< 0 or i >= n or j < 0 or j>=m or board[i][j] != suffix[0]):
            return False
        
        res = False
        board[i][j] = '#'
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for dx, dy in directions:
            res = backtrack(i+dx, j+dy, suffix[1:])
            if res: break

        board[i][j] = suffix[0]
        return res
    
    for i in range(n):
        for j in range(m):
            if backtrack(i,j, word): return True

    return False
    
