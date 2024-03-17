def solution(intervals, newIntervals):
    ## Iterate over array = 
    i = 0
    n = len(intervals)
    res = []

    while i < n:
        if intervals[i][1] < newIntervals[0]:
            res.append(intervals[i]) 
        elif intervals[i][0] > newIntervals[1]:
            break
        else:
            newIntervals[0] = min(intervals[i][0], newIntervals[0])
            newIntervals[1] = max(intervals[i][1], newIntervals[1])
        
        i+=1

    res.append(newIntervals)

    while i<n:
        res.append(intervals[i])
        i+=1

    return res