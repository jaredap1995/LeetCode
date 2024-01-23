import collections
def solution(nums):
    num1 = collections.Counter(nums).most_common(1)[0][0]
    correct = set(list(range(1,len(nums)+1)))
    num2 = list(correct.difference(set(nums)))[0]


    return [num1, num2]