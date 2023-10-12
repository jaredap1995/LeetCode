import collections
class Solution:
    def canVisitAllRooms(self, rooms):
        graph=collections.defaultdict(lambda: [])
        n=len(rooms)
        keys=set()
        for i in range(n):
            graph[i]=rooms[i]
            if rooms[i]==i:
                return False

        def DFS(key):
            if key in keys: #may not be right
                return 
            
            keys.add(key)
            for neighbor in graph[key]:
                DFS(neighbor)
        
        DFS(0)
        if list(keys)==[i for i in range(n)]:
            return True
        else:
            return False

rooms = [[1],[2],[3],[]]
rooms2 = [[1,3],[3,0,1],[2],[0]]
print(Solution().canVisitAllRooms(rooms))
            
        

        