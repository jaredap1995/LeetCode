import collections
from functools import lru_cache
from heapq import heappop, heappush
class Solution:
    def countRestrictedPaths(self, n: int, edges) -> int:
        # Create graph
        graph = collections.defaultdict(list)
        mod = 10**9+7

        for n1,n2, weight in edges:
            graph[n1].append((n2, weight))
            graph[n2].append((n1, weight))

        # Dijkstra algorithim using heapq
        distances = [float('inf')]*(n+1)
        # set node n to 0 as distance to istelf is zero
        distances[n]=0
        visited = set()
        # distance, node...pq is default a min priority queue and uses the first value (0 in thios case)
        pq = [(0,n)]

        while pq:
            dist, cur = heappop(pq)
            visited.add(cur)
            for neighbor, weight in graph[cur]:
                if neighbor not in visited:
                    new_dist = dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heappush(pq, (new_dist, neighbor))

        # DFS w/memo
        @lru_cache(None)
        def DFS(node):
            if node == n:
                return 1
            
            res = 0
            for neighbor , _ in graph[node]:
                if distances[neighbor] < distances[node]:
                    res += DFS(neighbor)
            return res

        res = DFS(1)
        return res % mod