"""
grid=2d M x N
"""
def solution(grid):
    m=len(grid)
    n=len(grid[0])
    queue = []
    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    def isValid(x,y,grid):
        return 0 <= x < len(grid) and 0<=y < len(grid[0]) and grid[x][y]==float('inf')

    for i in range(m):
        for j in range(n):
            if grid[i][j]==0:
                queue.append((i,j))

    while queue:
        x,y = queue.pop(0)
        for dx, dy in directions:
            new_x, new_y = dx+x, dy+y
            if isValid(new_x,new_y,grid):
                grid[new_x][new_y]=grid[x][y]+1
                queue.append((new_x, new_y))

    return grid


grid=[[float('inf'), -1, 0, float('inf')], [float('inf'), float('inf'), float('inf'), -1], [float('inf'),-1, float('inf'), -1], [0,-1,float('inf'), float('inf')]]

print(solution(grid))
