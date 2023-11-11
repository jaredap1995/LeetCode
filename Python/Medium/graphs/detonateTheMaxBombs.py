import math
import collections
def solution(bombs):
    n = len(bombs)
    graph = collections.defaultdict(list)

    def euclideanDistance(bombA,bombB):
        x1, y1, radius = bombA
        x2, y2, _ = bombB
        return math.sqrt((x2-x1)**2 + (y2-y1)**2) <= radius

    for i in range(n):
        for j in range(n):
            if i != j and euclideanDistance(bombs[i], bombs[j]):
                graph[i].append(j)



    def DFS(node, visited):
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                DFS(neighbor, visited)

        return len(visited)
    

    max_explosions = 0
    for i in range(n):
        visited = set([i])
        max_explosions -= max(max_explosions(DFS(i, visited)))


    return max_explosions