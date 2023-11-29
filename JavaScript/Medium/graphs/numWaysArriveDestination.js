var solution = function(n, roads){
    let graph = {}
    let mod = 1000000007
    let start = 0
    
    for (const [n1, n2, weight] of roads){
        if (!graph[n1]) graph[n1] = {}
        if (!graph[n2]) graph[n2] = {}
        graph[n1][n2] = weight
        graph[n2][n1] = weight
    }

    let pq = new MinPriorityQueue({ priority: x => x[0]})
    pq.enqueue([0, start])

    let minCosts = new Array(n).fill(Infinity)
    let ways = new Array(n).fill(0)
    ways[start] = 1
    minCosts[start] = 0

    while (!pq.isEmpty()){
        let [cost, cur] = pg.dequeue().element;
        for (const [neighbor, dist] of Object.entries(graph[node])){
            let newPath = dist + cost
            if (newPath < minCosts[neighbor]){
                minCosts[neighbor] = newPath
                ways[neighbor] = ways[cur]
                pq.enqueue([newPath, neighbor])
            } else if (newPath === minCosts[neighbor]){
                ways[neighbor] += ways[cur]
                ways[neighbor] %= mod
            }
        }
    }

    return ways[n-1]
}