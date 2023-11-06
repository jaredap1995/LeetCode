var solution = function (edges, patience) {
    let n = patience.length
    let graph = new Array(n).fill(0).map(() => [])
    let distances = new Array(n).fill(null)
    diatnces[0]=0

    for (const [n1,n2] of edges){
        graph[n1].push(n2)
        graph[n2].push(n1)
    }

    // populate distances array with BFS

    let queue = [0]
    while (queue.length) {
        let cur = queue.shift()
        for (const neighbor of graph[cur]) {
            if (distances[neighbor] === null){
                distances[neighbor] = distances[cur] + 1
                queue.push(neighbor)
            }
        }
    }

    var lastSendCalc = (node) => {
        if (2*distances[node] <= patience[node]) return 0
        if (2*distances[node] % patience[node] === 0) return 2*distances[node] - patience[node]
        return 2*distances[node] - (2*distances[node] % patience[node])
    }

    let maxTime = 0
    for (let i = 1; i<n; i++){
        lastSend = lastSendCalc(i)
        lastReceive = lastSend + 2*distances[i]
        maxTime = Math.max(maxTime, lastReceive)
    }

    return maxTime +1

}