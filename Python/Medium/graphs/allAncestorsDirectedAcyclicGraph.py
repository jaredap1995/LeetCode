import collections
def getAncestors(n, edges):
    graph = collections.defaultdict(list)
    for n1,n2 in edges:
        graph[n2].append(n1)

    def DFS(node, ancestorSet):
        for neighbor in graph[node]:
            if neighbor not in ancestorSet:
                ancestorSet.add(neighbor)
                DFS(neighbor, ancestorSet)

    answer = []
    for i in range(n):
        ansSet = set()
        DFS(i, ansSet)
        answer.append(sorted(list(ansSet)))

    return answer