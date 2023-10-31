import collections
def findTheCity(self, n, edges, distanceThreshold):
    graph = collections.defaultdict(dict)
    for n1, n2, distance in edges:
        graph[n1][n2] = distance
        graph[n2][n1] = distance

    def BFS(node):
        distances = [float('inf') if x != node else 0 for x in range(n)]
        queue = [node]

        while queue:
            cur = queue.pop(0)
            for neighbor,direct_distance in graph[cur].items():
                new_distance = direct_distance + distances[cur]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    queue.append(neighbor)

        return distances
    
    all_cities = [BFS(i) for i in range(n)]

    min_count = float('inf')
    result = -1

    for node, distance_arr in enumerate(all_cities):
        count = sum(1 for d in distance_arr if d <= distanceThreshold and d > 0)
        if count <= min_count:
            min_count = count
            result = node

    return result


