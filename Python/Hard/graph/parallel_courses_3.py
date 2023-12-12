import collections
import heapq

def dfs_my_solution(n, relations, time):
    if len(time)== 0:
        return time[0]
    if len(relations) == 0:
        return max(time)
    
    graph = collections.defaultdict(list)
    for n1, n2 in relations:
        graph[n2].append(n1)

    # Dummy value for index issue
    time.insert(0,0)

    dp = [-1] * (n+1)

    def dfs(node):
        if dp[node] != -1:
            return dp[node]
        
        max_time = dp[node]

        for neighbor in graph[node]:
            max_time = max(max_time, time[node] + dfs(neighbor))

        dp[node] = max_time
        return max_time
    
    sol = 0
    for i in range(1, n+1):
        sol = max(sol, dfs(i))

    return sol


def min_heap_solution(n, relations, time):
    graph = collections.defaultdict(list)
    in_degree = {node: 0 for node in range(n+1)}
    time.insert(0,0)

    for n1,n2 in relations:
        graph[n1].append(n2)
        in_degree[n2] += 1

    heap = []
    for node, degree in in_degree.items():
        if degree == 0:
            heapq.heappush(heap, (time[node], node))

    while heap:
        node_time, node = heapq.heappop(heap)

        for neighbor in graph[node]:
            in_degree[node] -= 1
            if in_degree[node] == 0:
                heapq.heappush(heap, (node_time + time[neighbor], neighbor))

    return node_time

def standard_BFS_Solution(n, relations, time):
    graph = collections.defaultdict(list)
    in_degree = collections.defaultdict(int)

    for n1, n2 in relations:
        graph[n1].append(n2)
        in_degree[n2] += 1

    # This returns a 0 of a non-existent key is accessed
    queue = [node for node in range(1, n+1) if in_degree[node] == 0]
    
    dist = [0] + time
    time.insert(0,0)
    while queue:
        cur = queue.pop(0)
        for neighbor in graph[cur]:
            dist[cur] = max(dist[neighbor], dist[cur] + time[neighbor])
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return max(dist)

