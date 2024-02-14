def solution(nums):
    pos = []
    neg = []
    for num in nums:
        if num >= 0: pos.append(num)
        else: neg.append(num)

    res = []
    for n1,n2 in zip(pos,neg):
        res.extend([n1,n2])
    
    return res
