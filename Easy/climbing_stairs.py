"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""


#Fibonacci sequence solution. Computationally expensive for large numbers dur to recursion
class Solution:
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
        

n=9
print(Solution().climbStairs(n))


#Dynamic Programming solution where variables are stored in a list and then used to calculate the next value
class Solution:
    def climbStairs_dynamic(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        ways = [0 for num in range(n)]
        ways[0] = 1
        ways[1] = 2
        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2] #Using fibonacci sequence to calculate the next value
        return ways[-1]  # return the last element
    
n=9
print(Solution().climbStairs_dynamic(n))


"""These solutions are based on the Fibonacci seqeunce, the first solution uses recursion while the second
uses a dynamic programming solution to speed up the computation. The first solution is elegeant but computationally expensive
for larger numbers as it requires the function to be called exponentially more times as the number increases. 
Climbstairs(5) requires the function to be broken down to climbstairs(4) and climbstairs(3) which themselves are broken
down further and so on. For large numbers this will create an excess amount of function calls.

In the du=ynamic solution twe create a list that is length (n) populated with 0's. We initialize the first two values
as 1 and 2 which represent the first two steps. We then use a for loop that calculates teh values of the fibonacci
seqeunce. Despite the for loop, this solution only needs to perform n operations, making it much more efficient 
than the top solution.
"""





