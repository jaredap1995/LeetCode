var solution = function(m,n,maxMove, startRow,startColumn){
    let moves = [[0,1], [1,0], [-1,0], [0,-1]]
    let memo = {}

    var dfs = (i,j,movesLeft) => {
        if (i < 0 || i ===m || j< 0 || j === n) return 1
        if (movesLeft === 0) return 0

        let key = i + ',' + j + ',' + movesLeft
        if (memo.hasOwnProperty(key)) return memo[key]

        let res = 0
        for (const [x,y] of moves){
            res = (res + dfs(i+x, j+y, movesLeft-1))%(10**9+7)
        }

        memo[key] = res
        return res
    }

    return dfs(startRow, startColumn, maxMove)
 }