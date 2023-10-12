import collections
class Solution:
    def allPathsSourceTarget(self, graph):
        n=len(graph)
        adj_list = collections.defaultdict(lambda: [])

        for i in range(n):
            adj_list[i]=(graph[i])

        paths=[]
        def DFS(cur, node):
            cur=cur+[node]
            if node == n-1:
                paths.append(cur)

            for neighbor in adj_list[node]:
                DFS(cur, neighbor)
            
        
        DFS([],0)
        return paths
    
graph=[[4,3,1],[3,2,4],[3],[4],[]]

print(Solution().allPathsSourceTarget(graph))



        