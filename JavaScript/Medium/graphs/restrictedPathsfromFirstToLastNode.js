var solution = function(n, edges) {
    let graph = new Array(n+1).fill(0).map(() => [])
    for (const [n1,n2,weight] of edges){
        graph[n1].push([n2, weight])
        graph[n2].push([n1, weight])
    }

    let distances = new Array(n+1).fill(Infinity)
    distances[n]=0

    var dijkstra = () => {
        const heap = new MinPriorityQueue({ priority: (x) => x[1]})
        heap.enqueue([n,0])
        while (heap.size()){
            let [curNode, dist] = heap.dequeue().element;
            for (const [neighbor, neighDistance] of graph[curNode]){
                let newDist = dist + neighDistance
                if (newDist < distances[neighbor]){
                    distances[neighbor] = newDist
                    heap.enqueue([neighbor, newDist])
                }
            }
        }
    }

    dijkstra()


    let dp = new Array(n+1).fill(-1)

    var DFS  = (cur, rCost) => {
        if (cur == n) return 1
        if (dp[cur] !== -1) return dp[cur]

        let counter = 0
        for (let [neighbor, _ ] of graph[cur]){
            if (distances[neighbor] < rCost){
                counter = (counter + DFS(neighbor, distances[neighbor]))
            }
        }

        return dp[cur] = counter
    }

    DFS(1, distances[1])
}