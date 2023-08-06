/**
 * @param {charachter [][]} board
 * @param {string} word
 * @return {boolean}
 */

var exist = function (board, word){
    let H = board.length
    let W = board[0].length

    var backtrack = (i,j,suffix) =>{
        if (suffix.length == 0){
            return true
        }

        if (i<0 || i==H || j <0 || j == W || board[i][j] != suffix[0]){
            return false
        }

        let ret = false
        board[i][j] = '#'

        let directions = [[-1,0], [1,0], [0,1], [0,-1]]
        for (let [dx,dy] of directions){
            ret = backtrack(i+dx,j+dy,suffix.slice(1))
            if (ret) {break}
        }

        board[i][j] = suffix[0]

        return ret
    }

    for (let i = 0; i<H; i++){
        for (let j =0; j<W; j++){
            if (backtrack(i,j,word)) {
                return true
            }
        }
    }
    return false

}