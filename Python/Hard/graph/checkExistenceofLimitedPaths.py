class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return
        
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        
        else:
            self.parent[xset] = yset
            self.rank[xset] += 1

class Solution:
    def distanceLimitedPathExists(self, n, queries, edgeList):
        uf = UnionFind(n)
        queries = [[i, ch] for i, ch in enumerate(queries)]
        queries.sort(key = lambda x: x[2])
        res = [0]*len(queries)
        edgeList.sort(key = lambda x: x[2])

        index = 0
        for idx, (node1, node2, weight) in enumerate(queries):
            while index < len(edgeList) and edgeList[2] < weight:
                uf.union(edgeList[idx][0], edgeList[idx][1])
                index += 1
            
            res[idx] = uf.find(node1) == uf.find(node2)

        return res


