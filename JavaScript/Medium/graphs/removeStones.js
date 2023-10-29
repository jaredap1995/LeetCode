var removeStones = function (stones) {
    let n = stones.length
    let x_dic = {}
    let y_dic = {}

    for (const [x,y] of stones){
        if (!x_dic[x]) x_dic[x] = []
        if (!y_dic[y]) y_dic[y] = []
        x_dic[x].push(y)
        y_dic[y].push(x)
    }

    let points = {}
    for (const [i,j] of stones){
        if (!points[i]){
            points[i] = {}
        }
        points[i][j]=0
    }

    var DFS = (i,j) => {
        if (points[i] && points[i][j] !== undefined) {
            delete points[i][j];
            for (const y of x_dic[i]) {
                if (points[i] && points[i][y] !== undefined) {
                    DFS(i, y);
                }
            }
            for (const x of y_dic[j]) {
                if (points[x] && points[x][j] !== undefined) {
                    DFS(x, j);
                }
            }
        }
       
    }

    let count = 0
    for (const [a,b] of stones){
        if (points[a] && points[a][b] !== undefined){
            DFS(a,b)
            count ++
        }
    }

    return n-count
}
    