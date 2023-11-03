import collections
import heapq
def maxProb(n, edges, succProb, start, end):
    graph = collections.defaultdict(dict)
    for prob, (n1,n2) in zip(succProb, edges):
        graph[n1][n2]=prob
        graph[n2][n1]=prob

    q=[[-1,start]]
    visited = set()

    while q:
        prob,node=heapq.heappop(q)
        if node in visited:
            continue
        if node == end:
            return -prob
        visited.add(node)
        for neighbor in graph[node]:
            heapq.heappush(q, (prob*graph[node][neighbor], neighbor))

    return 0

