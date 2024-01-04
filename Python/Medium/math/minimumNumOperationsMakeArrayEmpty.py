import collections
def solution(nums):
    counter = collections.Counter(nums)

    count = 0
    for val in counter.values():
        if val == 1:
            return -1
        count += val //3
        if val % 3:
            count += 1

    return count