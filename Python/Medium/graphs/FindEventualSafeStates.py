"""problem requires you to find the "safe" nodes in a graph. 

Safe is defined as only being able to reach a terminal node (one in which no directed edges protrude)


Can use topological sorting to go backwards starting from the edges

But much faster to use a DFS approach and mark the terminal/visiting nodes dynamically
"""

def solution(graph):
    n=len(graph)
    visited=[0]*n 
    result = []

    def DFS(node):
        if visited[node] > 0:
            return visited[node] ==2
        
        visited[node]=1
        for neighbor in graph[node]:
            if not DFS(neighbor):
                return False
            
        visited[node]=2
        return True
    
    for i in range(n):
        if DFS(i):
            result.append(i)

    return result