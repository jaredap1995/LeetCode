import collections
def solution(arr, k):
    c = sorted(collections.Counter(arr).most_common(), key = lambda x: x[1])
    u = set(arr)

    for key,v in c:
        while v >= 1 and k > 0:
            k -= 1
            v -= 1
            if v == 0:
                u.remove(key)
    
    return len(u)

