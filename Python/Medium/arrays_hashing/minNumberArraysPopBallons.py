def solution(points):
    res = 0
    maxa = float('-inf')
    points = list(sorted(points), key = lambda x: x[1])

    for i in range(len(points)):
        if maxa < points[i][0]:
            res +=1
            maxa = points[i][1]

    return res