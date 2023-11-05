var getAncestors = function(n,edges){
    let graph = new Array(n).fill(0).map(() => [])
    for(const [n1,n2] of edges){
        graph[n2].push(n1)
    }

    var DFS = (node, ancestorSet) => {
        for (const [neighbor] of graph[node]){
            if (!ancestorSet.has(neighbor)){
                ancestorSet.add(neighbor)
                DFS(neighbor, ancestorSet)
            }
        }
    }

    let answer = []
    for (let i = 0; i<n; i++) {
        let ansSet = new Set()
        DFS(i, ansSet)
        answer.push(Array.from(ansSet).sort((a,b) => a-b ))
    }

    return answer
}