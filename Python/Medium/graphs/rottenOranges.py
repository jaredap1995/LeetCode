from collections import deque

# Problem statement involves keeping track of a counter/iteration ==> BFS
class Solution(object):
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j,0))
                elif grid[i][j]==1:
                    fresh+=1


        if not fresh:
            return 0
        
        while q:
            r,c,count = q.popleft()

            #estbalish directions
            directions=[[0,1], [0,-1], [1,0], [-1,0]]

            #iterate in each direction
            for dx,dy in directions:
                rx,cy = r+dx, c+dy

                #Checking whether or not within bounds, if it is and is fresh then it is now rotten and added to deque
                if (0 <= rx < rows and 0 < cy < cols and grid[rx][cy]==1):
                    q.append((rx,cy,count+1))
                    grid[rx][cy]=2
                    fresh-=1

        if fresh >=1:
            return -1
        
        return count