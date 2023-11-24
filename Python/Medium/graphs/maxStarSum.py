import collections
def solution(vals, edges, k):
    graph = collections.defaultdict(list)

    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    sorted_vals = sorted(graph, key= lambda x: vals[x], reverse=True)

    maxStar = float('-inf')
    for i in range(len(vals)):
        maxNodes = graph[i][:k]
        curMax = vals[i]
        for node in maxNodes:
            if curMax + vals[node] > curMax:
                curMax = curMax + vals[node]

        if curMax > maxStar:
            maxStar = curMax

    return maxStar
