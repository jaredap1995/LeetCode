def solution(strs):
    res = ""
    for w in strs:
        if w[::-1] == w:
            res = w
            break
    return res

