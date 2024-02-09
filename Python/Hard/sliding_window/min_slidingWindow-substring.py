import collections

def solution(s,t):
    if s == t: return t
    left, right = 0,0
    start, end = 0,0

    window = collections.Counter()
    countT = collections.Counter(t)

    min_window_size = float('inf')

    need = len(t)

    while right < len(s):
        window[s[right]] += 1
        if s[right] in t:
            if window[s[right]] <= countT[s[right]]:
                need -= 1
        right +=1

        while need == 0:
            if right - left < min_window_size:
                min_window_size = right - left
                start, end = left, right
            
            if s[left] in countT:
                window[s[left]] -= 1
                if window[s[left]] < countT[s[left]]:
                    need += 1
            
            left += 1
    if min_window_size == float('inf'):
        return ""
    else:
        return s[start:end]
