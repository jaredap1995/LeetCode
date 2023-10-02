var findRedundantConnection = function (edges) {
    let graph = {}

    var DFS = (node1, node2) => {
        if (node1 === node2) {
            return true
        }

        visited.add(node1)

        for (let neighbor of (graph[node1] || [])) {
            if (!visited.has(neighbor)){
                if (DFS(neighbor, node2)) {
                    return true
                }
            }
        }
        return false
    }

    for(const [node1, node2] of edges) {
        visited = new Set()
        if (DFS(node1, node2)) {
            console.log([node1,node2])
            return [node1, node2]
        } else {
            if (!graph[node1]) {graph[node1]=[]}
            if (!graph[node2]) {graph[node2] = []}
            graph[node1].push(node2)
            graph[node2].push(node1)
        }
    }

}

const edges = [[1,2],[1,3],[2,3]]
findRedundantConnection(edges)