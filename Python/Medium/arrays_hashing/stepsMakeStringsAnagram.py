import collections
def solution(s,t):
    return (collections.Counter(s)-collections.Counter(t)).total()
