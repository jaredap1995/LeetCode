def solution(s):
    left = 0
    right = len(s) - 1

    while left < right and s[left] == s[right]:
        char = s[left]
        while left <= right and s[left] == char:
            left +=1
        while left <= right and s[right] == char:
            right -= 1

    return 0 if left > right else right - left + 1