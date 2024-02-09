def solution(nums):
    subsets = {-1: set()}

    nums.sort()
    for num in nums:
        divisors = []
        for key in subsets.keys():
            if num % key == 0:
                divisors.append(key)

        possibilities = [subsets[possibility] for possibility in divisors]

        longest_subset = max(possibilities, key = len)
        subsets[num] = longest_subset | {num}

    return max(subsets.values(), key = len)