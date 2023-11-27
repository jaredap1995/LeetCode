import heapq
class Solution:
    def minimumCost(self, start, target, specialRoads) -> int:
        def costCalc(coord1, coord2):
            return (abs(coord1[0]-coord2[0]) + abs(coord1[1] - coord2[1]))
        
        # Only include the values that end up being less than directly walking, if walking is less than there is no point in using special road
        specialRoads = tuple(((x1, y1), (x2, y2), cost) for x1,y1,x2,y2,cost in specialRoads if 
                             costCalc((x1,y1), (x2, y2)) > cost)
        
        visited = set()
        # [(cost, node)]
        pq = [(0, tuple(start))]
        direct = costCalc(start, target)

        while pq:
            cost, cur = heapq.heappop(pq)

            if cur in visited or cost > direct: continue

            direct = min(direct, cost + costCalc(cur, target))
            visited.add(cur)

            for rdStart, rdEnd, rdCost in specialRoads:
                heapq.heappush(pq, (cost + rdCost + costCalc(cur, rdStart)), rdEnd)
        
        return direct
