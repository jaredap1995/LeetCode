class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def is_valid(board, row, col):
            for i in range(row):
                if board[i]==col:
                    return False
            for i in range(row-1, -1,-1):
                if board[i]==col - (row-i):
                    return False
            for i in range(row-1, -1,-1):
                if board[i]==col + (row-i):
                    return False
            
        def convert_to_board(board):
            result=[]
            for row in board:
                result.append("." * row + "Q" + "." * (n-row-1))
            return result
        
        def backtrack(board, row):
            if row==n:
                result.append(convert_to_board(board[:]))
                return
            for col in range(n):
                if is_valid(board,row,col):
                    board[row]=col
                    backtrack(board, row+1)
                    board[row]=-1
                    
        result=[]
        board=[-1]*n
        backtrack(board, 0)
        return result