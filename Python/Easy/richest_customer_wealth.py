"""

You are given an m x n integer grid accounts where accounts[i][j] 
is the amount of money the ith customer has in the jth bank. 
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.

"""

accounts = [[1,5],[7,3],[3,5]]


class Solution(object):
    def maximumWealth(self, accounts):
        sums=[]
        for i in accounts:
            sums.append(sum(i))
        return max(sums)
        

print(Solution().maximumWealth(accounts))