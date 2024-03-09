import collections
def solution(nums):
    c = collections.Counter(nums)
    val = c.most_common(1)[0][1]
    return sum([i for i in c.values() if i == val])