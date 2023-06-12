"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait
 after the ith day to get a warmer temperature. If there is no future day for which this is possible, 
 keep answer[i] == 0 instead."""

temperatures = [73,74,75,71,69,72,71,73]
output=[1,1,4,2,1,1,0,0]


class Solution(object):
    def dailyTemperatures(self, temperatures):
        result=[0 for i in range(len(temperatures))]
        stack=[]
        n=len(temperatures)
        for idx, i in enumerate(temperatures):
            while stack and temperatures[idx]>temperatures[stack[-1]]:
                last_day=stack.pop()  
                result[last_day]=idx-last_day
            stack.append(idx)     
        return result
        
print(Solution().dailyTemperatures(temperatures))