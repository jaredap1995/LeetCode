var solution = function(n, edges) {
    let graph = new Array(n).fill(0).map(() => [])
    let visited = new Array(n).fill(0)

    for (const [n1,n2] of edges) {
        graph[n1].push(n2)
        graph[n2].push(n1)
    }

    let result = 0

    for (let i = 0; i<n; i++) {
        if (visited[i]===0){
            let queue = [i]
            visited[i]=1
            let curCount = 1

            while (queue.length) {
                let cur = queue.shift()
                for (const neighbor of graph[cur]){
                    if (visited[neighbor]===0){
                        visited[neighbor] = 1
                        curCount ++
                        queue.push(neighbor)
                    }
                }
            }

        result += curCount * (n-curCount) 
        }

    }

    return Math.floor(result/2)
}