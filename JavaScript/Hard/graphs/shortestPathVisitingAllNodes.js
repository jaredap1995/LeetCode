var solution = function(graph){
    let n = graph.length
    let allVisited = (1<<n) -1;
    let queue = []
    let visited = new Set()

    for (let i= 0; i< n; i++){
        queue.push([[1 << i], i, 0]);
        visited.add((1 <<i) * 16 + i)
    }

    while (queue.length > 0) {
        const [mask, node, dist] = queue.shift()

        if (mask === allVisited){
            return dist;
        }

        for (const neighbor of graph[node]){
            const newMask = mask | (1<<neighbor)
            const hashVal = newMask * 16 + neighbor

            if (!visited.has(hashVal)){
                visited.add(hashVal)
                queue.push([newMask, neighbor, dist + 1])
            }
        }
    }

return -1
}