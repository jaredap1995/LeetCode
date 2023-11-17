import collections
def DFSSolution(n, leftChild, rightChild):
    graph = collections.defaultdict(list)
    has_parent = [False]*n

    for i in range(n):
        if leftChild[i] != -1:
            graph[i].append(leftChild[i])
            has_parent[leftChild[i]] = True

        if rightChild[i] != -1:
            graph[i].append(rightChild[i])
            has_parent[rightChild[i]] = True

    # Determine if there is a single root and what it is
    roots = [i for i in range(n) if not has_parent[i]]

    # If more than one root...not valid
    if len(roots) != 1:
        return False
    
    visited = [False]*n
    def DFS(node):
        if visited[node] == True:
            return False
        visited[node] = True

        for neighbor in graph[node]:
            if not DFS(neighbor):
                return False

        return True
    
    return DFS(roots[0]) and all(visited)


"""
DFS approach is slower and suboptimal for this problem.

BFS is better

"""

def BFSSolution(n, righChild, leftChild):
    in_degree = [0]*n

    for i in range(n):
        if leftChild[i] != -1:
            in_degree[leftChild[i]] += 1

        if righChild[i] != -1:
            in_degree[righChild[i]] += 1

    
    # find root
    root = None
    for i in range(n):
        if in_degree[i] == 0:
            if root is None:
                root = i
            else:
                return False
            
    if root is None:
        return False
    

    visited = [False]*n
    queue = [root]

    while queue:
        cur = queue.pop(0)
        if visited[cur] == True:
            return False
        visited[cur] = True
        if leftChild[cur] != -1:
            queue.append(leftChild[cur])

        if righChild[cur] != -1:
            queue.append(righChild[cur])

    return sum(visited) == n