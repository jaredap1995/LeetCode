import math
import collections

class Solution:
    def minimumFuelCost(self, roads, seats):
        graph = collections.defaultdict(list)
        for node1, node2 in roads:
            graph[node1].append(node2)
            graph[node2].append(node1)

        total_liters=[0]

        def DFS(node, prev_node):
            size=1
            for neighbor in graph[node]:
                if neighbor == prev_node:
                    continue
                DFS(neighbor, node)

            if node != 0:
                total_liters[0] += math.ceil(size / seats)
            return size
        
        DFS(0, None)
        return total_liters[0]