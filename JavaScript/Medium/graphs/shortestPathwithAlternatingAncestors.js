var solution = function(n, blueEdges, rededges) {
    let graph = {}
    for (const [n1, n2] of blueEdges) {
        if (!graph[n1]) graph[n1] = {'blue': [], 'red': []}
        graph[n1]['blue'].push(n2)
    }

    for (const [n1,n2] of rededges) {
        if (!graph[n1]) graph[n1] = {'blue': [], 'red': []}
        graph[n1]['red'].push(n2)
    }

    let visited = new Set()
    let answer = new Array(n).fill(-1)
    // cur_node, prev_edge_color, dist
    let queue = [[0,None,0]]
    let colors = ['red', 'blue']

    while (queue.length){
        let [cur_node, prev_edge_color, dist] = queue.shift()
        if (answer[cur_node] === -1) answer[cur_node] = dist

        for (const color of colors){
            if (prev_edge_color !== color && graph[cur_node] && graph[cur_node][color]){
                for (const neighbor of graph[cur_node][color]){
                    let state = neighbor + ',' + color
                    if (!visited.has(state)) {
                        queue.push([neighbor, color, dist + 1])
                        visited.add(state)
                    }
                }
            }
        }
    }

    return answer
}