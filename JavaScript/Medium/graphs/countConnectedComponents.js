var countCompleteComponents = function(n, edges) {
    let graph = new Array(n).fill(0).map(() => [])
    for (const [node1, node2] of edges){
        graph[node1].push(node2)
        graph[node2].push(node1)
    }

    let visited = new Set()

    var BFS = (i) => {
        queue=[i]
        let nodes = 0
        let edges = 0

        while (queue.length){
            cur=queue.shift()
            nodes++
            for (const neighbor of graph[cur]){
                edges++
                if (!visited.has(neighbor)){
                    visited.add(neighbor)
                    queue.push(neighbor)
                }
            }
        }

        return [nodes, edges/2]
    }

    let connected = 0

    for (let i = 0; i<n; i++){
        if (!visited.has(i))
        {
            let [nodes, edges] = BFS(i)
            if (edges == nodes *(nodes-1)/2){ connected ++}
        }

    }
    
    return connected
};