def solution(s):
    def newS(s):
        start = "@"
        for i in s:
            start += "#"+i
        start += "#$"
        return start
    
    right,center = 0,0
    count = 0
    q = newS(s)
    dp = [0]*len(q)

    for i in range(1, len(q)-1):
        #Set mirror
        iMirror = center- (i-center)

        #Optimization
        if right > i:
            dp[i]= min(iMirror, right-i)

        while q[i+1+dp[i]] == q[i-1-dp[i]]:
            dp[i]+=1

        if i + dp[i] > right:
            # center is set to i
            center = i
            # right boundary is set to i + dp[i]
            right = i + dp[i]

        # Even and odd count addition
        count = (dp[i]//2) + dp[i]%2

    
    return count