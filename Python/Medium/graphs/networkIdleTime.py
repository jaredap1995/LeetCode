import collections
def networkBecomesIdle(edges, patience):
    graph = collections.defaultdict(list)

    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    queue = [0]
    distances = [None]*len(patience)
    distances[0] = 0

    while queue:
        cur = queue.pop(0)
        for neighbor in graph[cur]:
            if not distances[neighbor]:
                distances[neighbor] = distances[cur] + 1
                queue.append(neighbor)

    def lastSencCalc(node):
        if (2*distances[node] <= patience[node]):
            return 0
        if (2*distances[node] % patience[node] == 0):
            return 2*distances[node] - patience[node]
        return 2*distances[node] - (2*distances[node] % patience[node])
    
    max_time = 0
    for i in range(1, len(patience)):
        last_send = lastSencCalc(i)
        last_receive = last_send + 2*distances[i]
        max_time = max(max_time, last_receive)

    return max_time +1

