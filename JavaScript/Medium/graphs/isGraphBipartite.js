var solution = function(graph) {
    let n = graph.length
    let color = new Array(n).fill(0)

    for (let i = 0; i<n; i++) {
        if (color[i] !== 0) continue

        let queue = [i]
        color[i] = 1

        while (queue.length) {
            let cur = queue.shift()
            for (const neighbor of graph[cur]) {
                if (color[neighbor] === 0) {
                    color[neighbor] = -color[cur]
                    queue.push(neighbor)
                } else if (color[neighbor] === color[cur]){
                    return false
                }
            }
        }
    }

    return true
}