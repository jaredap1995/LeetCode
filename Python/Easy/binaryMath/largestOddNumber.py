import collections
def solution(s):
    c = collections.Counter(s)
    o = ["0"]*c["0"]
    l = ['1']*c['1']
    if len(l) > 1:
        return l[:-1] + o + l[-1]
    elif len(l) == 1:
        return o+l[-1]
    else:
        return o