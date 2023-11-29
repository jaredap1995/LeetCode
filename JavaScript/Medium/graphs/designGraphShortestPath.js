var Graph = function(n, edges){
    this.edges = edges;
    this.n = n;

    this.graph = new Array(n).fill(0).map(() => [])

    for (const [n1,n2, weight] of edges){
        this.graph[n1].push([n2, weight])
    }
}


Graph.prototype.addEdge = function(edge){
    this.graph[edge[0]].push([edge[1], edge[2]])
}


Graph.prototype.shortestPath = function(node1, node2){
    let minDists = new Array(n).fill(Infinity);
    minDists[node1] = 0

    let pq = new MinPriorityQueue({ prirority: x => x[0]})
    pq.enqueue([0, node1])

    while (!pq.isEmpty()){
        let [cost, cur] = pq.dequeue().element;

        if (cur === node2) return cost;

        if (cost > minDists[cur]) continue

        for (const [neighbor, dist] of this.graph[cur]){
            let newDist = cost + dist;
            if (newDist < minDists[neighbor]){
                minDists[neighbor] = newDist
                pq.enqueue([newDist, neighbor])
            }
        }
    }


    return minDists[node2] === Infinity ? -1 : minDists[node2]
}


