import collections
class Solution:
    def findJudge(self, n, trust):
        graph = collections.defaultdict(lambda: [])

        nodes = set()
        for n1,n2 in trust:
            graph[n1].append(n2)
            nodes.add(n1)
            nodes.add(n2)

        print(graph)
        print(nodes)
        for val in nodes:
            if val not in graph.keys():
                print(val)
                trust_count = 0
                for l in graph.values():
                    if val in l:
                        trust_count +=1
                        if trust_count == n-1:
                            return val
        
        return -1

n = 4
trust = [[1,3],[1,4],[2,3]]

print(Solution().findJudge(n,trust))
        