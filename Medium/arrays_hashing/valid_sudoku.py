"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules."""


class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                num = board[i][j]
                box_index = (i // 3) * 3 + j // 3

                if (num in rows[i]) or (num in columns[j]) or (num in boxes[box_index]):
                    return False

                rows[i].add(num)
                columns[j].add(num)
                boxes[box_index].add(num)

        return True
    

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


print(Solution().isValidSudoku(board))
print((4//3)*3+0//3)


"""This solution works by creating three lists of sets wthat are each 9 elements long (consistent with the length/box size of a sudoku board).
The sets only allow unique elements and correspond to each row/column/box. 
We use a nested loop to iterate through the rows and then each value in the columns for each row.
If it is not a number we continue.
Otherwise we grab the number (the index for the row and bcolumn is just [i][j]) and the box index which requires a little math and 
understanding of the operators. After that it is a simple if statement to check if the number already exists within the set
for the row, column, or box by passing the index of tghe current location.
Othwerwise we add it to teh set and move on."""