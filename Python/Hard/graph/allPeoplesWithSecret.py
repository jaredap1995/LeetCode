import collections
import heapq
def solution(n,meetings,firstPerson):
    graph = collections.defaultdict(list)
    for n1,n2,time in meetings:
        graph[n1].append((n2, time))
        graph[n2].append((n1,time))

    heap = [(0,0), (0,firstPerson)]
    res = set()

    while heap:
        time, cur = heapq.heappop(heap)

        if cur not in res:
            res.add(cur)
        else:
            continue

        for neighbor, meetingTime in graph[cur]:
            if meetingTime >= time:
                heapq.heappush(heap, (meetingTime, neighbor))

    return res