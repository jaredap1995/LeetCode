import collections
import heapq
class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

        self.graph = collections.defaultdict(list)
        for n1,n2,weight in self.edges:
            self.graph[n1].append((n2, weight))

    def addEdge(self, edge):
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1, node2):
        pq = [(0, node1)]
        minDists = [float('inf')]*self.n
        minDists[node1] = 0

        while pq:
            cost, cur = heapq.heappop(pq)

            if cur == node2: return cost

            if cost > minDists[cur]: continue

            for neighbor, dist in self.graph[cur]:
                newPath = dist + cost
                if newPath < minDists[neighbor]:
                    minDists[neighbor] = newPath
                    heapq.heappush(pq, (newPath, neighbor))

        
        return -1 if minDists[node2] == float('inf') else minDists[node2]

    