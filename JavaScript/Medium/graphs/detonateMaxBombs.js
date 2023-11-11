var solution = function(bombs){
    var euclidean = (bombA, bombB) => {
        let [x1,y1, radius] = bombA
        let [x2, y2, _] = bombB
        
        return Math.sqrt((x2-x1)**2 + (y2-y2)**2) <= radius
    }

    let n = bombs.length
    let graph = new Array(n).fill(0).map(() => [])

    for (let i = 0; i<n; i++){
        for (let j = 0; j<n; j++){
            if (i!==j && euclidean(bombs[i], bombs[j])){
                graph[i].push(j)
            }
        }
    }

    var DFS = (node, visited) => {
        for (const neighbor of graph[node]){
            if (!visited.has(neighbor)){
                visited.add(neighbor)
                DFS(neighbor, visited)
            }
        }

        return visited.size
    }

    let maxDetonations = 0;
    for (let i= 0; i< n; i++){
        let visited = new Set([i])
        maxDetonations = Math.max(maxDetonations, DFS(i, visited))
    }

    return maxDetonations
}