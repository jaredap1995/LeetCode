from heapq import heappop, heappush
def solution(grid):
    m, n = len(grid), len(grid[0])
    dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    dx = [0,0,0,1,-1] #As described in problem
    dy = [0,1,-1,0,0]
    pq = [(0,0,0)] #Start at origin with cost of 0
    dist[0][0] = 0 #distance to get to origin is also 0

    while pq:
        cost, x,y = heappop(pq)
        if visited[x][y]:
            continue

        visited[x][y] = 1

        for i in range(1,5):
            x2, y2 = dx[i] + x, dy[i] + y
            if x2 < 0 or y2 < 0 or x2 >= m or y2 >= n:
                continue
            
            if i == grid[x][y]:
                if dist[x2][y2] > cost:
                    dist[x2][y2] = cost
                    heappush(pq, (cost, x2, y2))
            
            else:
                if dist[x2][y2] > cost + 1:
                    dist[x2][y2] = cost + 1
                    heappush(pq, (cost+1, x2, y2))

    return dist[m-1][n-1]

