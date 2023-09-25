var orangesRotten = function(grid) {
    let rows = grid.length
    let cols = grid[0].length
    let count = 0

    let q = new Array()
    let fresh = 0

    for (let i = 0; i<rows; i++) {
        for (let j = 0; j<cols; j++) {
            if (gridp[i][j]==2) {
                q.push([i,j,0])
            }
            else if (grid[i][j]==1){
                fresh+=1
            }
        }
    }

    if (!fresh) {return 0}

    while (q.length) {
        const [r,c,curCount] = q.shift()
        count = curCount

        let directions = [[0,1], [1,0], [0,-1], [-1,0]]

        for (const [dx, dy] of directions){
            let rx = r+dx
            let cy = c+dy

            if (0<=rx && rx < rows && 0 < cy && cy < cols && grid[rx][cy]==1) {
                q.push([rx,cy,count+1])
                grid[rx][cy]=2
                fresh-=1
            }
        }
    }

    if (fresh>=1) { return -1}

    return count

}