"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

print(11//2)
print(5%4)



class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        
        rows,columns =len(matrix), len(matrix[0])
        low,high=0,rows*columns-1

        while low <= high:
            mid=(low+high)//2
            num=matrix[mid//columns][mid % columns]

            if num==target:
                return True
            elif num<target:
                low=mid+1
            else:
                high=mid-1

        return False