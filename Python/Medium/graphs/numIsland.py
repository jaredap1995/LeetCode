class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(i,j):
            if grid[i][j]=='1':
                grid[i][j]='x'
                if i<m-1:
                    dfs(i+1,j)
                if i>0:
                    dfs(i-1,j)
                if j<n-1:
                    dfs(i,j+1)
                if j>0:
                    dfs(i,j-1)


        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    res+=1
                    dfs(i,j)
        
        return res
    

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

sol = Solution()
print(sol.numIslands(grid))
    




from collections import deque



class Solution:
    def numIsland(self, grid):
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])

        def bfs(i,j):
            q=deque()
            q.append((i,j))
            while q:
                curRow, curCol = q.popleft()
                for dx, dy in directions:
                    r = curRow + dx
                    c = curCol + dy
                    if r in range(rows) and c in range(cols) and grid[r][c]=='1':
                        grid[r][c]=='/'
                        q.append((r,c))
            return grid

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    bfs(i,j)
                    count+1

        return count