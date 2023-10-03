import collections

def validTree(nodes, edges):
    graph = collections.defaultdict(lambda: [])

    for node1,node2 in edges:
        graph[node1].append(node2)
        graph(node2).append(node1)

    visited = set()
    def DFS(root):
        visited.add(root)
        for n in graph[root]:
            if n in visited:
                continue
            DFS(n)

    DFS(0)
    return len(visited)==nodes and len(edges)==nodes-1
