import collections
class Solution:
    def buildMatrix(self, k: int, rowConditions, colConditions):
        matrix = [[0 for _ in range(k)] for _ in range(k)]
        
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
        for u in row_order:
            r, c = row_order[u], col_order[u]
            matrix[r][c] = u + 1
        return matrix