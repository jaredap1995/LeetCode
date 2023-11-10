import collections
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites, queries):

        """
        Brute Force Approach, too slow for larger inputs
        
        """

        # Prerequisites has no cycles
        if not prerequisites:
            return [False]*numCourses

        graph = collections.defaultdict(list)
        for prereq, course in prerequisites:
            graph[course].append(prereq)
        

        def DFS_determine_indirect(prereq, course):
            if prereq in graph[course]:
                return True
        
            if not graph[course]:
                return False

            for neighbor in graph[course]:
                if DFS_determine_indirect(prereq, neighbor):
                    return True

            return False


        
        output = []

        for query in queries:
            prereq, course = query[0], query[1]
            bool_ = DFS_determine_indirect(prereq, course)
            output.append(bool_)

        return output
    
numCourses = 3
isReachable = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
print(isReachable)


def correctSolution(n,numCourses,prerequisites,queries):
    graph = collections.defaultdict(list)
    isReachable = collections.defaultdict(set)

    for prereq, course in prerequisites:
        graph[prereq].append(course)

    def DFS(node):
        if node in isReachable:
            return isReachable[node]
        
        for neighbor in graph[node]:
            isReachable[node].add(neighbor)
            isReachable[node].update(DFS(neighbor))

        return isReachable[node]
    
    for i in range(numCourses):
        DFS(i)

    return [course in isReachable[prereq] for prereq, course in queries]

        

    

