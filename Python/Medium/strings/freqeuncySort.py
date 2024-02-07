import collections
def solution(str):
    ans = []
    c = collections.Counter(str)

    for k,v in c.most_common():
        ans.append(k*v)
    
    return "".join(ans)


s = 'treeee'
print(solution(s))
