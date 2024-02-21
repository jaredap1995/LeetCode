def solution(left, right):
    while right > left:
        right = right & (right -1)
    return right & left