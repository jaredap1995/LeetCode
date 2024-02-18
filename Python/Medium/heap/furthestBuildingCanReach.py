import heapq
def solution(heights, bricks, ladders):
    n = len(heights)
    heap = []
    for i in range(1, n):
        diff = heights[i]-heights[i-1]
        if diff > 0:
            heapq.heappush(heap, diff)
        if len(heap) > ladders:
            bricks -= heapq.heappop(heap)
            if bricks < 0: return i-1

    return n-1