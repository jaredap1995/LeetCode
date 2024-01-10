import collections
def solution(root, start):
    def adjList(root):
        graph = collections.defaultdict(list)
        queue = [root]

        while queue:
            cur = queue.pop(0)
            if cur.left != None and cur.right != None:
                graph[cur.val].extend([cur.right.val, cur.left.val])
                graph[cur.right.val].append(cur.val)
                graph[cur.left.val].append(cur.val)
                queue.extend([cur.right, cur.left])
            if cur.left.val != None and cur.right.val == None:
                graph[cur.left.val].append(cur.val)
                graph[cur.val].append(cur.left.val)
                queue.append(cur.left)
            if cur.left.val == None and cur.right.val != None:
                graph[cur.right.val].append(cur.val)
                graph[cur.val].append(cur.right.val)
                queue.append(cur.right)

        return graph
    
    graph = adjList(root)

    queue = [start]
    visited = set()

    levels = -1
    while queue:
        levels += 1
        for i in range(len(queue)):
            cur = queue.pop(0)
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    queue.append(neighbor)


    return levels
    

