var dfs_solution = function(n, relations, time) {
    if (time.length == 0){
        return time[0]
    }
    if (relations.length == 0){
        return Math.max(...time)
    }


    let graph = new Array(n+1).fill(0).map(() => [])
    for (let [n1,n2] of relations){
        graph[n2].push(n1)
    }

    let dp = new Array(n+1).fill(-1)
    // time.unshift(0)

    var DFS = (node) => {
        if (dp[node] != -1){
            return dp[node]
        }

        cur_time = time[node-1]

        for (const neighbor of graph[node]){
            cur_time = Math.max(cur_time, time[node-1] + DFS(neighbor-1))
        }

        dp[node] = cur_time

        return cur_time
    }

    let res = 0
    for (let i = i; i<n+1; i++){
        res = Math.max(res, DFS(i))
    }

    return res
}


var BFS = function(n, relations, time){
    let graph = new Array(n+1).fill(0).map(() => [])
    let inDegree = new Array(n+1).fill(0)

    for (const [n1,n2] of relations){
        graph[n1].push(n2)
        inDegree[n2] ++
    }

    let dist = [].concat(0, time)
    let queue = Array.from({length: n}, (_, i) => i + 1).filter((val) => inDegree[val] === 0)

    while (queue.length){
        let cur = queue.shift()
        for (const neighbor of graph[node]){
            dist[neighbor] = Math.max(dist[neighbor], dist[cur] + time[neighbor-1])
            inDegree[neighbor] --
            if (inDegree[neighbor] === 0) {
                queue.push(neighbor)
            }
        }
    }

    return Math.max(...dist)
}


var minHeap = function(n, relations, time){
    let graph = new Array(n+1).fill(0).map(() => [])
    let indegree = new Array(n+1).fill(0)

    for (const [n1,n2] of relations){
        graph[n1].push(n2)
        indegree[n2] ++
    }

    let heap = new MinPriorityQueue({priority: x => x[0]})
    time.unshift(0)
    Array.from({length: n}, (_,i) => i + 1).filter(i => indegree[i] === 0)
        .forEach((val) => heap.enqueue([time[val], val]))

    while (!heap.isEmpty()){
        var [time_, cur] = heap.dequeue().element;
        for (const neighbor of graph[cur]){
            indegree[neighbor] --
            if (indegree[neighbor] === 0) heap.enqueue([time_ + time[neighbor], neighbor])
        }
    }

    return time_
}