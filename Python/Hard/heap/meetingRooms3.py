from heapq import heappop, heappush
def solution(n, meetings):
    busy = []
    available = [i for i in range(n)]
    count = [0]*n
    meetings.sort()

    for start, end in meetings:
        while busy and busy[0][0] <= start:
            _ , room = heappop(busy)
            heappush(available, room)

        if available:
            room = heappop(available)
            heappush(busy, (end, room))

        else:
            time, room = heappop(busy)
            heappush(busy, (time + end- start, room))
    
        count[room] += 1

    return count.index(max(count))