def solution(n, edges):
    indegree = {i: 0 for i in range(n)}
    for n1, n2 in edges:
        indegree[n2] += 1

    champ = []
    for k, v in indegree.items():
        if v == 0:
            champ.append(k)

    return champ[0] if len(champ) == 1 else -1
