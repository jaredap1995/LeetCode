def solution(s):
    start = 0
    end = len(s) -1
    res = 0

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while start < end:
        if s[start] in vowels:
            res +=1 

        if s[end] in vowels:
            res -=1

        start +=1
        end -=1

    return True if res == 0 else False

