import collections
class Solution:
    def loudAndRich(self, richer, quiet):
        richer_count = [0 for _ in range(len(quiet))]
        graph = collections.defaultdict(list)
        answer = [idx for idx in range(len(quiet))]

        for rich, poor in richer:
            graph[rich].append(poor)
            richer_count[poor] += 1

        queue = [] #In queue starts 2,4,5,6
        for person, rich_count in enumerate(richer_count):
            if not rich_count:
                queue.append(person)

        while queue:
            cur = queue.pop(0)
            quieter = answer[cur] 
            print(quieter)
            for poorer in graph[cur]: 
                print(poorer)
                quieter_richer = answer[poorer] #
                print(quieter_richer)
                answer[poorer]=min(quieter, quieter_richer, key = lambda x: quiet[x]) 
                print(answer[poorer])
                richer_count[poorer] -=1 
                if not richer_count[poorer]: 
                    queue.append(poorer) 


        return answer
    
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]

print(Solution().loudAndRich(richer, quiet))