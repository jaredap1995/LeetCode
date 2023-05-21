"""An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

"""


class Solution(object):
    def checkValid(self, matrix):
        length=len(matrix)
        rows = [set() for _ in range(length)]
        columns = [set() for _ in range(length)]

        for i in range(length):
            for j in range(length):
                num=matrix[i][j]

                if (num in rows[i]) or (num in columns[j]):
                    return False
                
                rows[i].add(num)
                columns[j].add(num)

        return True

matrix = [[1,2,3],[3,1,2],[2,3,1]]
print(Solution().checkValid(matrix))
