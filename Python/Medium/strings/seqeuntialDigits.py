def solution(low, high):
    allDigits = '123456789'
    res = []
    for windowSize in range(len(str(low)), len(str(high))+1):

        for start in range(0, 10 - windowSize):
            end = start+windowSize
            curDigit = int(allDigits[start:end])
            if curDigit >= low and curDigit <= high:
                res.append(curDigit)

    return res
