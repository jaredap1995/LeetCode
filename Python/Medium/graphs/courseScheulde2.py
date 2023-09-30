class Solution:
    def findOrder(self, numCourses, prerequisites):
        dic = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            dic[course].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)

            for pre in dic[course]:
                if dfs(pre)==False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        
        return output