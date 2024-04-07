def solution(s):
    leftMin = 0
    leftMax = 0

    for char in s:
        if char == '(':
            leftMax += 1
            leftMin += 1
        elif char == ')':
            leftMin -= 1
            leftMax -= 1
        else:
            leftMin -= 1
            leftMax += 1

        if leftMax < 0: return False
        if leftMin < 0: leftMin = 0

    return True if leftMin == 0 else False