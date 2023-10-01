"""
In an undirected graph, the presence of a back edge (an edge that connects a node to one of its ancestors in the DFS tree)
"""
import collections
class Solution: 
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(lambda: [])

        def DFS(parent, node):
            if node == parent:
                return True
            
            visited.add(node)

            for neighbor in graph[parent]:
                if neighbor not in visited:
                    if DFS(neighbor, node):
                        return True
                    
            return False
        

        for node1, node2 in edges:
            visited = set()
            if DFS(node1, node2):
                return [node1, node2]
            else:
                graph[node1].append(node2)
                graph[node2].append(node1)
        
        return None


