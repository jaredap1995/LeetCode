import { MinPriorityQueue } from 'collections.js';

var solutionDijskstra = function(n, flights, src, dst, k) {
    let graph = new Array(n).fill(0).map(() => [])
    for (const [n1,n2, weight] of flights){
        graph[n1].push([n2, weight])
    }

    // dp array[i][j] shows the cost of reaching a node j with stops i from source
    let dp = new Array(k+2).fill(null).map(() => new Array(n).fill(Infinity))

    let queue = new MinPriorityQueue({ priority: x => x[0]})
    // [cost, node, stops]
    queue.enqueue([0, src, 0])

    while (!queue.isEmpty()){
        let [cost, node, stops] = queue.dequeue().element;

        if (node === dst) return cost

        if (stops > k) continue

        for (const [neighbor, weight] of graph[node]){
            let newCost = cost + weight
            if (newCost < dp[stops + 1][neighbor]){
                dp[stops+1][neighbor] = newCost
                queue.enqueue([newCost, neighbor, stops + 1])
            }
        }
    }

    return dp[k+1][dst] === Infinity ? -1 : dp[k+1][dst]

}

var solutionBellmanFord = function(n, flights, src, dst, k) {
    let prices = new Array(n).fill(Infinity)
    prices[src] = 0

    // Modified Bellman Ford to find cheapest path with at most k stops (iterate k+1) instead of iterating n-1 times
    for (let i = 0; i<k+1; i++){
        let tempPrices = [...prices]
        for (let [start, end, cost] of flights){
            // Have not yet found way to reach this node
            if (prices[start] === Infinity) continue
            if (prices[start] + cost < tempPrices[end]){
                tempPrices[end] = prices[start] + cost
            }
        }
        // Relaxed nodes for this iteration, move to next one
        prices = [...tempPrices]
    }

    return prices[dst] === Infinity ? -1 : prices[dst]
}