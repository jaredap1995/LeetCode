var solution = function(img){
    m = img.length
    n = img[0].length

    var gridHelp = (row, col) => {
        let total = 0
        let count = 0

        let top = Math.max(0, row-1)
        let bottom = Math.min(m, row + 2)
        let left = Math.max(0, col - 1)
        let right = Math.min(n, row + 2)

        for (let r = 0; r< row; r++){
            for (let c = 0; c<col; c++){
                total += img[r][c]
                count ++
            }
        }
    
        return Math.floor(total/count)

    }

    let output = new Array(m).fill(0).map(() => new Array(n).fill(0))

    for (let col = 0; col < n; col ++){
        for (let row = 0; row < m; row ++){
            output[row][col] = gridHelp(row, col)
        }
    }

    return output

}