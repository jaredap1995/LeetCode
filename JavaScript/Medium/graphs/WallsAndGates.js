// Shortest Distance (nearest gate)===BFS approach
// popleft in JS is array.shift
// incrementing inf to 1 

var solution = function(grid) {
    let m = grid.length
    let n = grid[0].length
    let queue = []
    const directions = [[1,0], [0,1], [-1,0], [0,-1]]

    for (let i=0; i<m; i++){
        for (let j = 0; j<n; j++){
            if (grid[i][j]===0){
                queue.push([i,j])
            }
        }   
     }

     var isValid = (grid, x, y) => {
        return 0 <= x && x<m && 0<=y && y<n && grid[x][y]===Infinity
     }

     while (queue.length) {
        cur = queue.shift()
        x=cur[0], y=cur[1]
        for (const [dx, dy] of directions) {
            new_x = x+dx
            new_y = y+dy
            if (isValid(grid, new_x, new_y)){
                grid[new_x][new_y]=(grid[x][y]===Infinity ? 1 : grid[x][y]+1)
                queue.push([new_x, new_y])
            }
        }
     }

     return grid
}


grid = [
    [Infinity,  -1,        0,        Infinity],
    [Infinity,  Infinity,  Infinity,  -1      ],
    [Infinity,  -1,        Infinity,  -1      ],
    [0,         -1,        Infinity,  Infinity]
]

console.log(solution(grid))
