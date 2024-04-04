import collections
def solution(s):
    c = collections.Counter()
    res = 0
    for char in res:
        if char == '(':
            c[0] += 1
        elif char == ')':
            c[0] -= 1
        res = max(res, c[0])

    return res
