class Solution(object):
    def findCenter(self, edges):
        count_goal = len(edges)
        res=[0]*(count_goal+2)
        nums=[num for edge in edges for num in edge]
        for i in nums:
            res[i]+=1
            if res[i]==count_goal:
                return i
            

edges = [[1,2],[2,3],[4,2]]

print(Solution().findCenter(edges))