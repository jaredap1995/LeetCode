def solution(edges, node1, node2):
    # No need for defaultdict graph because each node only has a single edge
    # We can just use edges and iterate
    n = len(edges)
    distances1 = [-1]*n
    distances2 = [-1]*n

    # Create DFS functions to check if node has edge and traverse path
    # Store values in specific result array
    def DFS(node, distances):
        dist = 0
        while distances[node] == -1 and node != -1:
            distances[node] = dist
            dist +=1
            node = edges[node]

    # Iterate over result arrays for each node and compare

    DFS(node1, distances1)
    DFS(node2, distances2)

    min_value = float('inf')
    result = -1
    for i in range(n):
        if distances1[i] != -1 and distances2[i] != -1:
            max_val = max(distances1[i], distances2[i])
            if max_val< min_value:
                min_value = max_val
                result = i

    return result