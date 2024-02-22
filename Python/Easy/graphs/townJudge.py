import collections
def solution(trust, n):
    trusts = collections.defaultdict(int)
    trusted_by = collections.defaultdict(int)

    for a,b in trust:
        trusts[a] += 1
        trusted_by[b] += 1

    for i in range(1,n+1):
        if trusts[i] == 0 and trusted_by[i] == n-1:
            return i
    
    return -1
