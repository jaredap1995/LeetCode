class Solution:
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        island_key = {}

        def dfs(i,j):
            if i < 0 or i >=m or j < 0 or j >=n or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 'x'
            length =1

            length += dfs(i-1, j)
            length += dfs(i+1, j)
            length += dfs(i, j-1)
            length += dfs(i, j+1)

            return length


        island_index = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    length = dfs(i,j)
                    island_key[island_index] = length
                    island_index +=1

        return max(island_key.values())
    

grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

sol = Solution()
print(sol.maxAreaOfIsland(grid))