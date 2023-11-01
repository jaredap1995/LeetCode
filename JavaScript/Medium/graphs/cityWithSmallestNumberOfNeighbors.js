// Dijkstra's Algorithm

var findTheCity = function(n, edges, distanceThreshold){
    let graph = {}
    for (const [n1,n2, distance] of edges) {
        if (!graph[n1]) graph[n1] = {}
        if (!graph[n2]) graph[n2] = {}
        graph[n1][n2] = distance
        graph[n2][n1] = distance
    }

    var BFS = (i) => {
        let distances = new Array(n).fill(Infinity)
        distances[i] = 0
        let queue = [i]

        while (queue.length) {
            cur = queue.shift()
            if (graph[cur]) {
                for (const [neighbor, directDistance] of Object.entries(graph)) {
                    let newDistance = distances[cur] + directDistance
                    if (newDistance < distances[neighbor]) {
                        distances[neighbor] = newDistance
                        queue.push(neighbor)
                    }
                }
            }
        }

        return distances
    }

    let results = []
    for (let i = 0; i<n; i++) {
        results.push(BFS(i))
    }

    let minCount = Infinity
    let result = -1

    results.forEach((value, index) => {
        let count = value.filter(d => d<= distanceThreshold && d >0).length
        if (count <= minCount){
            minCount = count
            result = index
        }
    })

    return result

}