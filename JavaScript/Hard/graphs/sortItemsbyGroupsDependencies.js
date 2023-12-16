var sortItems = function(n, m, group, beforeItems) {
    const graph = Array.from({ length: m + n }, () => [])
    const inDegree = new Array(n+m).fill(0)

    for (let i = 0; i<group.length; i++ ){
        if (group[i] == -1) continue // Not a group
        graph[n + group[i]].push(i)
        inDegree[i] ++
    }

    for (let currentNode = 0; currentNode < beforeItems.length; currentNode ++){
        for (const dependencyNode of beforeItems[currentNode]){
            const dependencyGroup = group[dependencyNode] === -1 ? dependencyNode : n + group[dependencyNode]
            const currentGroup = group[currentNode] === -1 ? currentNode: n + group[currentNode]
            if (dependencyGroup === currentGroup) {
                // Intra-group dependency...pushing currentItem that is AFTER dependencyItem
                graph[dependencyNode].push(currentNode)
                inDegree[currentNode] ++
            } else {
                // Inter-group dependency
                graph[dependencyGroup].push(currentGroup)
                inDegree[currentGroup] ++
            }
        }
    }



    var dfs = (res, graph, indegree, n, cur) => {
        // If current node is less than n is has InDegree of 0, push it, otherwise it is a group
        if (cur < n) res.push(cur)
        indegree[cur] = -1
        for (let neighbor of graph[cur]){
            indegree[neighbor] -- 
            if (indegree[neighbor] === 0) dfs(res, graph, indegree, n, neighbor)
    }
    }

    const res = []
    for (let i = 0; i< n+m; i++){
        if (inDegree[i] === 0) dfs(res, graph, inDegree, n, i)
    }

    return res.length === n ? res: []

}