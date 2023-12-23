def solution(directions):
    directions = list(directions)

    mapper = {"N": (0,1),
            "E": (1,0),
            "W": (-1,0),
            "S": (0,-1)}


    pos = (0,0)

    test = set()
    test.add(pos)

    for dir in directions:
        pointx = pos[0] + mapper[dir][0]
        pointy = pos[1] + mapper[dir][1]
        pos = (pointx, pointy)
        if pos in test:
            return True
        else:
            test.add(pos)

    return False

directions = "SS"
print(solution(directions=directions))

