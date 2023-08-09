/**
 * @param {number} n
 * @return {string [][]}
 */

var nQueens = function(n) {
    var isValid = (board, row, col) => {
        for (let i = 0; i<row; i ++){
            if (board[row]==col) { return false }
        }

        for (let i = row-1; i>= 0; i--) {
            if (board[row] == col - (row - i)) { return false}
               }
        
        for (let i = row-1; i>=0; i--) {
            if (board[row] == col + (row - i)) { return false}
        } 
    
        return true
    }

    var convertToString = (board) => {
        res = []
        for (let row of board) {
            res.push(".".repeat(n-row)+"Q"+".".repeat(n-row-1))
        }
        return res
    }

    var backtrack = (board, row) => {
        if (row == n) {
            result.push(convertToString(board.slice()))
            return
        }

        for (let col = 0; col < n; col ++) {
            if (isValid(board, row, col)) {
                board[row] = col
                backtrack(board, row+1)
                board[row] = -1
            }
        }
    }

    result = []
    board = new Array(n).fill(-1)
    backtrack(board, 0)
    return result

}

// n=4
// board = [0,2,1,2]
// row=board[1]
// console.log('.'.repeat(n-row))