import collections
def calcUnreachableNodes(n, edges):
    graph = collections.defaultdict(list)
    for n1,n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    visited = [0]*n
    result = 0
    queue = []

    for i in range(n):
        if visited[i]==0:
            queue.append(i)
            visited[i]=1
            curCount = 1

            while queue:
                cur = queue.pop(0)
                for neighbor in graph[cur]:
                    if visited[neighbor]==0:
                        visited[neighbor]=1
                        curCount +=1
                        queue.append(neighbor)
            result += curCount * (n-curCount)

    return result //2


n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]

print(calcUnreachableNodes(n,edges))