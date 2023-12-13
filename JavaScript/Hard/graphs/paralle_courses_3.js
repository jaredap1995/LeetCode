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