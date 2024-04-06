def solution(s):
    stack = []
    for i,char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)

    res = []
    for i, char in enumerate(s):
        if stack and i == stack[0]:
            stack.pop(0)
            continue
        res.append(char)

    return ''.join(res)