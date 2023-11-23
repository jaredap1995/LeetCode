import collections
def solution(n, edges):
    if n == 1: return [0]

    graph = collections.defaultdict(list)
    degree = collections.defaultdict(int)
    for n1,n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)
        degree[n1] += 1
        degree[n2] += 1

    leaves = [i for i in range(n) if len(graph[i]) == 1]

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            for neighbor in graph[leaf]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
        
        leaves = new_leaves

    return leaves

