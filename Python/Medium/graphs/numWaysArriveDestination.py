import collections
import heapq

def solution(n, roads):
    mod = 1000000007
    graph = collections.defaultdict(dict)
    start = 0

    for n1,n2,weight in roads:
        graph[n1][n2] = weight
        graph[n2][n1] = weight

    # (cost, startNode)
    pq = [(0, start)]
    minCosts = [float('inf')]*n
    minCosts[start] = 0
    ways = [0]*n
    ways[start]=1

    while pq:
        cost, cur = heapq.heappop(pq)
        for neighbor, dist in graph[cur].items():
            newPath = cost + dist
            if newPath < minCosts[neighbor]:
                minCosts[neighbor] = newPath
                ways[neighbor] = ways[cur]
                heapq.heappush(pq, (newPath, neighbor))
            elif newPath == minCosts[neighbor]:
                ways[neighbor] += ways[cur]
                ways[neighbor] %= mod

    return ways[n-1]

