import collections
def solution(n, connections):
    if len(connections) < n-1:
        return -1

    graph = collections.defaultdict(list)
    for node1, node2 in connections:
        graph[node1].append(node2)
        graph[node2].append(node1)

        visited = set()
        components = 0

        def BFS(i):
            queue=[i]
            while queue:
                cur=queue.pop(0)
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                BFS(i)
                components+=1

    return components - 1