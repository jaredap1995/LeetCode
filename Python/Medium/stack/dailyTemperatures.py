def solution(temperatures):
    n = len(temperatures)
    stack = []
    answer = [0]*n
    for i in range(n):
        while stack and temperatures[i]> temperatures[stack[-1]]:
            cur = stack.pop()
            answer[cur] = i-cur
        stack.append(i)

    return answer