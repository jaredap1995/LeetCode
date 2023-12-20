class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n
        self.size = 1 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset: #They have the same parent, no union is needed
            return False #We return False here for boolean check in problem
        
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        else:
            self.parent[xset] = yset #does not matter which we choose
            self.rank[xset] += 1

        self.size +=1
        return True #Again, not typical but returning boolean for problem

    """
    For this problem we will increment size and use it to count the size of Alice and Bob components

    In a typical use case 'size = n' and is decremented to count number of distinct connected components
    """

class Solution:
    def solution(self, edges, n):
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        ans = 0

        for type_, node1, node2 in edges:
            if type_ == 3 and (not uf_alice(node1-1, node2-1) or not uf_bob(node1-1, node2-1)):
                ans += 1

        for type_, node1, node2 in edges:
            if type_ == 2 and not uf_bob(node1-1, node2-1):
                ans +=1
            elif type_ == 1 and not uf_alice(node1-1, node2-1):
                ans +=1

        return ans if uf_alice.size == n and uf_bob.size == n else -1
