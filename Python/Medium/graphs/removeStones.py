import collections
def removeStones(stones):
    def DFS(a,b):
        points.discard((a,b))
        for y in x_dic[a]:
            if (a,y) in points:
                DFS(a,y)

        for x in y_dic[b]:
            if (x,b) in points:
                DFS(x,b)

        x_dic = collections.defaultdict(list)
        y_dic = collections.defaultdict(list)

        points = {(i,j) for i,j in stones}

        for i, j in stones:
            x_dic[i].append(j)
            y_dic[j].append(i)
        
        count = 0
        for a,b in stones:
            if (a,b) in points:
                DFS(a,b)
                count+=1

        return len(stones)-count