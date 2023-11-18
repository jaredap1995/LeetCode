import collections
from functools import lru_cache
from heapq import heappop, heappush
class Solution:
    def countRestrictedPaths(self, n: int, edges) -> int:
        g, mod = collections.defaultdict(list), 10 ** 9 + 7
        # dfs + memo

        @lru_cache(None)
        def dfs(cur):
            if cur == n:
                return 1
            res = 0
            for (nei, w) in g[cur]:
                # no need  to maintain set, it's impossible to go back
                if dist[cur] > dist[nei]: 
                    res += dfs(nei)
            return res
        # dijkstra
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        visited = set()
        pq = [(0, n)]
        while pq:
            d, cur = heappop(pq)
            visited.add(cur)
            for (nei, w) in g[cur]:
                if nei not in visited:
                    new_dist = d + w
                    if new_dist < dist[nei]:
                        heappush(pq, (new_dist, nei))
                        dist[nei] = new_dist
        res = dfs(1)
        return res % mod