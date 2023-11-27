var solution = function(start, target, specialRoads){
    var costCalc = (coord1, coord2) => {
        return Math.abs(coord1[0] - coord2[0]) + Math.abs(coord1[1] - coord2[1])
    }

    dist = costCalc(start, target)

    let newRoads = specialRoads.map(([x1,y1,x2,y2,cost]) => [[x1,y1], [x2,y2], cost])

    let visited = new Set()
    let pq = new MinPriorityQueue({ priority: x => x[0]})
    // [cost, node]
    pq.enqueue([0,start])

    while (!pq.isEmpty()){
        let [cost, node] = pq.dequeue().element;

        if (visited.has(node) || cost > dist) continue

        dist = Math.min(dist, cost + costCalc(node, target))
        visited.add(node)

        for (const [rdStart, rdEnd, rdCost] of newRoads){
            pq.enqueue([cost + rdCost + costCalc(node, rdStart), rdEnd])
        }
    }

    return dist
}