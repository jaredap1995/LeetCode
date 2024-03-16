def solution(order, s):
    temp = []
    res = ""
    for char in s:
        if char in order:
            idx = order.index(char)
            temp.append((char, idx))

    temp = list(sorted(temp , key = lambda x: x[1]))
    for val in temp:
        res += val[0]

    idx = 0
    length = len(s)

    while idx < length:
        val = s[idx]
        if val not in order:
            res += val
    
    return val

