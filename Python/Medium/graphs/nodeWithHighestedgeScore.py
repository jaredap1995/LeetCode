import collections
def solution(edges):
    n = len(edges)
    result = [0]*n

    for idx, val in enumerate(edges):
        result[val] += idx

    return result.index(max(result))

