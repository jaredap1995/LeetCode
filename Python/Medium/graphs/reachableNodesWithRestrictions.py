import collections
class Solution:
    def reachableNodes(self, n: int, edges, restricted) -> int:
        restricted = set(restricted)
        graph = collections.defaultdict(list)
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()

        queue = [0]
        visited.add(0)
        while queue:
            cur = queue.pop(0)
            for neighbor in graph[cur]:
                if neighbor not in restricted and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
        
        return len(visited)
    

n = 7
edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
restricted = [4,5]

# print(Solution().reachableNodes(n,edges, restricted=restricted))


class Solution:
    def reachableNodes2(self, n: int, edges, restricted) -> int:
        restricted = set(restricted)
        graph = collections.defaultdict(list)
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()

        visited.add(0)

        def DFS(node):
            for neighbor in graph[node]:
                if neighbor not in restricted and neighbor not in visited:
                    visited.add(neighbor)
                    DFS(neighbor)

        DFS(0)

        
        return len(visited)
    
print(Solution().reachableNodes2(n,edges, restricted=restricted))