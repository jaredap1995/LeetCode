def solution(grid):
    n = len(grid)
    def checkVals(a,b):
        ops = 0
        for i in range(n):
            for j in range(n):
                if i >= n//2:
                    portionOfY = j == n//2
                else:
                    portionOfY = (i==j) or (i == (n-1-j))

                if (portionOfY and grid[i][j] != a) or ((not portionOfY) and grid[i][j] != b):
                    ops += 1

        return ops

    res = float('Infinity')
    for i in range(3):
        for j in range(3):
            if i != j:
                res = min(res, checkVals(i,j))
    
    return res
