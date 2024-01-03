import collections
def solution(nums):
    if len((set(nums))) == len(nums):
        return [nums]
    
    counter = collections.Counter(nums)
    max_val = max(counter.values())
    res = [[] for _ in range(max_val)]

    i = 0
    while i<max_val+1:
        for k,v in counter.items():
            if counter[k] == 0: continue
            res[v-1].append(k)
            counter[k] -= 1
        i += 1
    
    return res

