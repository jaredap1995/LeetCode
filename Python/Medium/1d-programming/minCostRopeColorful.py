def solution(colors, neededTime):
    start = 0
    end = 1
    sol = 0

    while end < len(colors):
        if colors[start] == colors[end]:
            temp = end
            while temp < len(colors):
                if colors[temp] == colors[start]: temp += 1
                else: break
            group = neededTime[start:temp]
            groupTime = sum(group) - max(group)
            sol += groupTime

            start = temp
            end = start +1

        else:
            start += 1
            end += 1
    
    return sol