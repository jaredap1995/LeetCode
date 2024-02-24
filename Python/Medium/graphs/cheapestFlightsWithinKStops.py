import collections
import heapq

# Problem is essentially a modified dijkstra with dynamic programming. Getting the shortest path within k stops. Need to epxlore everything wihin k stops
def solution(n, k, flights, src, dst):
    dp = [float('inf')*(n) for _ in range(k+2)] #k + 2 because we need dummy row for indexing and an extra row because (k stops + destination)
    queue = [(0,src,0)] #cost, node, stops
    dp[0][src] = 0 #DP state represents [number of stops][node]

    graph = collections.defaultdict(list)
    for n1, n2, cost in flights:
        graph[n1].append((n2, cost))

    while queue:
        cost, cur, stops = heapq.heappop(queue)

        if cur == dst: return cost

        if stops > k: continue

        for neighbor, weight in graph[cur]:
            curStop = weight + cost
            if curStop < dp[stops + 1][neighbor]:
                dp[stops + 1][neighbor] = curStop
                heapq.heappush(queue, (curStop, neighbor, stops + 1))

    return -1 if dp[k+1][dst] == float('inf') else dp[k+1][dst]


    