import collections
def colution(n, redEdges, blueEdges):
    # create your dictionary that goes {source: {'red': [destinations], 'blue': [destinations]}
    graph = collections.defaultdict(lambda: {'red': [], 'blue': []})
    for n1,n2 in redEdges:
        graph[n1]['red'].append(n2)
    for n1,n2 in blueEdges:
        graph[n1]['blue'].append(n2)

    visited = set()
    # Start a queue for BFS with (cur_node, last_color, distance_from_root)
    queue = [(0, None, 0)]
    answer = [-1]*n

    while queue:
        cur_node, last_color, dist = queue.pop(0)
        if answer[cur_node] == -1:
        # If distance hasn't been visited/set, set the distance = equal to cur_distance
            answer[cur_node] = dist
        for color in ['red', 'blue']:
            if color != last_color:
                for neighbor in graph[cur_node][color]:
                    if (neighbor, color) not in visited:
                        visited.add((neighbor, color))
                        queue.append((neighbor, color, dist + 1))

    return answer