def solution(s):
    max_score = 0
    ones_right = s.count('1')
    zeros_left = 0

    for i in range(len(s) -1):
        zeros_left += s[i] == '0'
        ones_right -= s[i] == '1'
        max_score = max(max_score, zeros_left+ones_right)

    return max_score