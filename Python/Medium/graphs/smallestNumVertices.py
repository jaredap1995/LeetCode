import collections

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        goal = [i for i in range(n)]
        ends=list(set([end for _, end in edges]))
        res=[]
        for val in goal:
            if val not in ends:
                res.append(val)
        return res

n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
print(Solution().findSmallestSetOfVertices(n, edges))

def correct(n, edges):
    ends=[False]*n
    for _, end in edges:
        ends[end]=True

    return [i for i in range(n) if not ends[i]]