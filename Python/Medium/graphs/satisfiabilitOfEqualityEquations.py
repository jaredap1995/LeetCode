def solution(equations):
    parents = {}
    diff = []

    def find(x):
        if x not in parents: return x
        else: return find(parents[x])

    for eq in equations:
        a, b = eq[0], eq[3]
        if eq[1] == "=":
            x = find(a)
            y = find(b)
            if x != y:
                parents[y] = x
        else:
            diff.append((a,b))

    return all(find(a) != find(b) for a,b in diff)