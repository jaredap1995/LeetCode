var solution = function (n, connections) {
    let graph = new Array(n).fill(0).map(() => [])
    for (const [node1, node2] of connections){
        graph[node1].push([node2, false])
        graph[node2].push([node1, true])
    }

    let reachZero = new Array(n).fill(false)
    reachZero[0]=true
    let count= 0;

    var DFS = (node) => {
        for (const [neighbor, direction] of graph[node]){
            if (reachZero[neighbor]){continue}
            if (!direction) {count ++}
            reachZero[neighbor]=true
            DFS(neighbor)
        }
    }

    DFS(0)
    return count
}

connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
n = 6

console.log(solution(n, connections))