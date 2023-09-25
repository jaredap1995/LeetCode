class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        #  0 = unvisited, 1 = visiting, 2 = visited
        visited = [0]*numCourses

        def DFS(course):
            if visited[course]==1:
                return True
            if visited[course]==2:
                return False
            
            visited[course]=1

            for pre in graph[course]:
                if DFS(pre):
                    return True
                
            visited[course]=2
            return False
        
        for i in range(numCourses):
            if DFS(i):
                return False
        
        return True

            

