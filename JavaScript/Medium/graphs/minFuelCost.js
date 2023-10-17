var minimumFuelCost = function(roads, seats) {
    let graph = new Array(roads.length+1).fill(0).map(() => [])
    let totalLiters = 0

    for (const [node1, node2] of roads) {
        graph[node1].push(node2)
        graph[node2].push(node1)
    }

    var DFS = (node, prevNode) => {
        let size = 1;
        for (let neighbor of graph[node]) {
            if (neighbor === prevNode) {continue}
            size += DFS(neighbor, node)
        }
        if (node != 0) {
            totalLiters += Math.ceil(size/seats)
        }
        return size
    }

    DFS(0, null)
    return totalLiters
}