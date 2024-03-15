def solution(arr, goal):
    res = 0
    pre = {0:1}
    cumsum = 0
    for i in arr:
        cumsum += i
        res += pre.get(cumsum - goal, 0)
        pre[cumsum] = pre.get(cumsum, 0)+1

    return res
