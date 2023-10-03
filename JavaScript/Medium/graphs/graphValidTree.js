var graphValidTree = function (n, edges) {
    let graph = {}

    for (const [n1, n2] of edges) {
        if (!graph[n1]) {graph[n1] = []}
        if (!graph[n2]) {graph[n2] = []}
        graph[n1].push(n2)
        graph[n2].push(n1)
    }

    let visited = new Set()
    var DFS = (root) => {
        visited.add(root)
        for (let node of graph[root]) {
            if (visited.has(node)){
                continue
            }
            DFS(node)
        }
    }

    DFS(0)
    console.log(visited.size)
    console.log(visited)
    return (visited.size==n && edges.length==n-1)
}

n=5
edges=[[0,1], [0,2],[0,3], [1,4]]

console.log(graphValidTree(n, edges))

