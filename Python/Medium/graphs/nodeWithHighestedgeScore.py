import collections
def solution(edges):
    n = len(edges)
    result = [0]*n

    for idx, val in enumerate(edges):
        result[val] += idx

    return result.index(max(result))



watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
Output: ["B","C"] 
graph = collections.defaultdict()
n = len(friends)
for i in range(n):
    graph[i]=(watchedVideos[i], friends[i])

cur = 0
for tup in graph[cur]:
    print(None, tup[1])