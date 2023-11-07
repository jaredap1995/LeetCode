import collections
def gardenNoAdj(n, paths):
    graph = collections.defaultdict(list)
    for n1, n2 in paths:
        graph[n1].append(n2)
        graph[n2].append(n1)

    ans = [0]*n

    for garden in range(1, n+1):
        available = {1,2,3,4}
        for neighbor in graph[garden]:
            if ans[neighbor-1] in available:
                available.remove(ans[neighbor-1])
        ans[garden-1]=available.pop()

    return ans

