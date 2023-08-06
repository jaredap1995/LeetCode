class Solution:
    def exist(self, board, word):
        self.h = len(board)
        self.w = len(board[0])
        self.board = board

        for i in range(self.h):
            for j in range(self.w):
                if self.backtrack(i,j,word):
                    return True
        
        return False
    
    def backtrack(self,i,j,suffix):
        if len(suffix) == 0:
            return True
        
        if i<0 or i ==self.h or j <0 or j == self.w or self.board[i][j] != suffix[0]:
            return False
        
        ret = False
        self.board[i][j] = '#'
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in directions:
            ret = self.backtrack(i+dx, j+dy, suffix[1:])
            if ret: break

        self.board[i][j] = suffix[0]

        return ret