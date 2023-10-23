import collections
class Solution:
    def minReorder(self, n: int, connections):
        graph=collections.defaultdict(lambda: [])
        for node1, node2 in connections:
            graph[node1].append([node2, False])
            graph[node2].append([node1, True])

        reachZero=[False]*n
        reachZero[0]=True
        count=0

        def DFS(node):
            nonlocal count
            for neighbor, boolean in graph[node]:
                if reachZero[neighbor] is True:
                    continue
                if not boolean:
                    count+=1
                reachZero[neighbor]=True
                DFS(neighbor)
        
        DFS(0)
        return count


n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

print(Solution().minReorder(n, connections))