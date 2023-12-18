import collections
def shortestPathLength(graph):
    n = len(graph)
    queue = collections.deque([(1 << i, i, 0) for i in range(n)])
    visited = set(( 1<< i, i ) for i in range(n))


    while queue:
        mask, node, dist = queue.popleft()
        if mask == (1<<n) - 1:
            return mask
        
        for neighbior in graph[node]:
            new_mask = mask | (1 << neighbior)
            if (new_mask, neighbior) not in visited:
                queue.append((new_mask, neighbior, dist + 1))
                visited.add((new_mask, neighbior))
