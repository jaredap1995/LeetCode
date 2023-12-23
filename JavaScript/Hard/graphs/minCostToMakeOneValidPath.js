var solution = function(grid){
    let m = grid.length
    let n = grid[0].length
    let dist = new Array(m).fill(0).map(() => new Array(n).fill(Infinity))
    let visited = new Array(m).fill(0).map(n)(() => new Array(n).fill(0))
    let pq = new MinPriorityQueue({ priority: x => x[0] })
    let dx = [0,0,0,1,-1]
    let dy = [0,1,-1,0,0]


    // cost, x, y
    pq.enqueue([0,0,0])
    dist[0][0] = 0

    while (!pq.isEmpty()){
        let [cost, x, y] = pq.dequeue().element;
        if (visited[x][y] === 1) continue

        visited[x][y] = 1

        for (let i = 1; i < 5; i++){
            let x2 = dx[i] + x, y2 = dy[i] + y;

            if (x2 < 0 || y2 < 0 || x2>=m || y2>= n) continue

            if (grid[x][y] === i){
                if (dist[x2][y2] > cost){
                    dist[x2][y2] = cost
                    pq.enqueue([cost, x2, y2])
                }
            } else {
                if (dist[x2][y2] > cost + 1){
                    dist[x2][y2] = cost + 1
                    pq.enqueue([cost + 1, x2, y2])
                }
            }
        }
    }

    return dist[m-1][n-1]
}