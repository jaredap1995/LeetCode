import collections
class Solution:
    def minScore(self, n: int, roads) -> int:
        graph = collections.defaultdict(dict)
        for n1, n2, distance in roads:
            graph[n1][n2]=distance
            graph[n2][n1] = distance

        min_val = float('inf')
        def DFS(node, visited):
            nonlocal min_val
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in graph[node]:
                distance = graph[node][neighbor]
                if distance < min_val:
                    min_val = distance
                print(min_val)
                DFS(neighbor, visited)


        visited = set()
        DFS(1, visited)
        return min_val
    


n = 4
roads = [[1,2,9],[2,3,6],[2,4,7],[1,4,5]]

print(Solution().minScore(n, roads))

        