def isBipartite(graph):
    color = len(graph)
    for i in range(len(color)):
        if color[i] != 0:
            continue
            
        queue = [i]
        color[i] = 1

        while queue:
            cur = queue.pop(0)
            for neighbor in graph[cur]:
                if color[neighbor] == 0:
                    color[neighbor] = -color[cur]
                    queue.append(neighbor)
                elif color[neighbor] == color[cur]:
                    return False
    
    return True