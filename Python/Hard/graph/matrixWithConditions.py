import collections
def solution(rowConditions, colConditions, k):
    res = [[0]*k for _ in range(k)]

    def topologicalSort(condition):
        graph = collections.defaultdict(list)
        in_degree = [0]*k
        for a,b in condition:
            graph[a].append(b)
            in_degree[b-1] +=1

        queue = []
        for i, val in enumerate(in_degree):
            if val == 0:
                queue.append(i+1)
        
        order  = []
        while queue:
            cur = queue.pop(0)
            order.append(cur)

            for neighbor in graph[cur]:
                in_degree[neighbor-1] -= 1
                if in_degree[neighbor - 1] == 0:
                    queue.append(neighbor)

        return order
    

    row_order = topologicalSort(rowConditions)
    col_order = topologicalSort(colConditions)

    if len(row_order) < k or len(col_order) < k:
        return []
    

    for row, val in enumerate(row_order):
        col = col_order.index(val)
        res[row][col] = val

    return res
        



