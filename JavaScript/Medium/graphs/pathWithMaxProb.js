var maxProbability = function(n, edges, succProb, start_node, end_node) {
    let probs = new Array(n).fill(0);
    let graph = probs.reduce((accumulator, _, index) => accumulator.set(index, []), new Map());
    edges.forEach(([node1, node2], index) => {
        graph.get(node1).push([node2, succProb[index]])
        graph.get(node2).push([node1, succProb[index]])
    });

    queue = [[start_node, 1]]
    probs[start_node]=1

    while(queue.length){
        [curNode, curProb] = queue.shift();
        for (const [neighbor, neighborProb] of graph.get(curNode)){
            if ((curProb * neighborProb) > probs[neighbor]){
                probs[neighbor] = curProb * neighborProb
                queue.push([neighbor, probs[neighbor]])
            }
        }
    }

    return probs[end_node]
}