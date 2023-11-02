var minPath = function(n, roads) {
    let graph = {}

    for (const [n1,n2, distance] of roads){
        if (!graph[n1]) graph[n1] = {}
        if (!graph[n2]) graph[n2] = {}
        graph[n1][n2] = distance
        graph[n2][n1] = distance
    }

    var DFS = (node, visited ) => {
        if (!visited.has(node)) {
            return
        }

        visited.add(node)

        for (const neighbor of Object.keys(graph[node])){
            let distance = graph[node][neighbor]
            if (distance < minVal) minVal = distance
            DFS(neighbor, visited)
        }
    }

    let visited = new Set()
    let minVal = Infinity
    DFS(1, visited)

    return minVal
}