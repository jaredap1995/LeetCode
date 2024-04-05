def solution(s):
    stack = []
    for i in range(len(s)):
        if stack and abs(ord(s[i]) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(s[i])

    return ''.join(stack)