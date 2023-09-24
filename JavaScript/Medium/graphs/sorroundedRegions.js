// An 'O' should not be flipped if it is on border

/**
 * @param {charachter[][]} board
 * @return {void}
 */

var solve = function (board) {
    if (!board || board.length ==0) {return board}

    let row = board.length
    let col = board[0].length

    var DFS = (i,j) => {
        if (i>=row || j >=n || i<=0 || j<=0 || board[i][j]!=='O') return

        // Placeholder
        board[i][j]='A'

        DFS(i+1, j)
        DFS(i-1, j)
        DFS(i,j+1)
        DFS(i,j-1)
    }

    // Boundary DFS
    for (let i =0; i<row; i++){
        if (board[i][0]=='O') {DFS(i, 0)}
        if (board[i][col-1]=='O') {DFS(i, col-1)}
    }

    for (let j = 0; j<col; j++) {
        if (board[0][j]=='O') {DFS(0,j)}
        if (board[row-1][j]) {DFS(row-1,j)}
    }

    // Reset Values
    for (let i = 0; i<row; i++){
        for (let j= 0; j<col; j++) {
            if (board[i][j] =='O') {board[i][j]='X'}
            if (board[i][j]=='A') {board[i][j]='O'}
        }
    }

    return board
}