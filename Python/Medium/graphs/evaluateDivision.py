import collections

def solution(equations, values, queries):
    graph = collections.defaultdict(dict)
    for i in range(equations):
        graph[equations[i][0]][equations[i][1]]=values[i]
        graph[equations[i][1]][equations[i][0]]=1/values[i]

    def DFS(src, dst, visited):
        if src not in graph or dst not in graph:
            return -1

        if dst in graph[src]:
            return graph[src][dst]
        
        for neighbor in graph[src]:
            if neighbor not in visited:
                visited.add(neighbor)
                temp = DFS(neighbor, dst, visited)
                if temp == -1:
                    continue
                else:
                    return temp * graph[src][neighbor]
        return -1
    
    result = []
    for start, end in queries:
        result.append(DFS(start, end, set()))

    return result





