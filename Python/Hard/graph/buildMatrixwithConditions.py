import collections
class Solution:
    def buildMatrix(self, k: int, rowConditions, colConditions):
        matrix = [[0]*k]*k
        
        def topo_sort(condition):
            order = {}
            in_degree = [0 for _ in range(k)]
            g = collections.defaultdict(list)
            for start, end in condition:
                g[start - 1].append(end - 1)
                in_degree[end - 1] += 1
            
            dq = collections.deque()
            for i in range(k):
                if in_degree[i] == 0: dq.append(i)
            
            i = 0
            while dq:
                u = dq.popleft()
                order[u] = i
                for v in g[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0: dq.append(v)
                i += 1
            
            return order
        
        row_order, col_order = topo_sort(rowConditions), topo_sort(colConditions)
        if len(row_order) != k or len(col_order) != k: return []
        print('theirs')
        for u in row_order:
            r, c = row_order[u], col_order[u]
            matrix[r][c] = u + 1
            print(matrix)


    
        return matrix
    

def solution(k, rowConditions, colConditions):
    matrix = [[0]*k for _ in range(k)]

    def topo_sort(conditions):
        order = {}
        graph = collections.defaultdict(list)
        inDegree = collections.defaultdict(int)
        for before, after in conditions:
            graph[before-1].append(after-1)
            inDegree[after-1] += 1

        queue = []
        for node in range(k):
            if inDegree[node] == 0: queue.append(node)

        i = 0
        while queue:
            node = queue.pop(0)
            order[node] = i 
            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0: queue.append(neighbor)
            i += 1

        return order
    

    col_order, row_order = topo_sort(colConditions), topo_sort(rowConditions)
    if len(col_order) != k or len(row_order) != k: return []
    print('mine')
    for node in row_order:
        r, c = row_order[node], col_order[node]
        matrix[r][c] = node + 1 #for indexing
        print(matrix)
        

    return matrix

rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]

Solution().buildMatrix(3,rowConditions,colConditions)
solution(3, rowConditions, colConditions)