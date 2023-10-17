class Solution:
    def costConnectAllPoints(self, points):
        class Union_Find:
            def __init__(self, points):
                self.parents=list(range(len(points)))

            def find(self, x):
                if self.parents[x] != x:
                    return self.find(self.parents[x])
                
                else: 
                    return x
            
            def union(self, x, y):
                self.parents[self.find(y)]=self.parents[x]

        
        # Find weights for all points (manhattan distance)
        arr = []
        for i in range(len(points-1)):
            for j in range(1, len(points)):
                distance = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                arr.append((distance, i, j))
        
        # sort to iterate over array in ascending order
        arr.sort()

        total_cost=0
        uf=Union_Find(points)
        for distance, point1, point2 in arr:
            if uf.find(point1) != uf.find(point2):
                uf.union(point1, point2)
                total_cost+=distance

        return total_cost