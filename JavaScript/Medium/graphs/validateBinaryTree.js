var DFSSolution = function(n, leftChild, rightChild){
    let graph = new Array(n).fill(0).map(() => [])
    let hasParent = new Array(n).fill(false)

    for (let i = 0; i<n; i++){
        if (leftChild[i] != -1){
            graph[i].push(leftChild[i])
            hasParent[leftChild[i]]=true
        }

        if (rightChild[i] != -1){
            graph[i].push(rightChild[i])
            hasParent[rightChild[i]]= true
        }
    }

    let roots = []
    for (let i = 0; i<n; i++){
        if (!hasParent[i]){
            roots.push(i)
        }
    }

    if (roots.length != 1) return false

    let visited = new Array(n).fill(false)
    var DFS = (node) => {
        if (visited[node]==true) return false
        visited[node] = true

        for (const neighbor of graph[node]){
            if (!DFS(neighbor)) return false
        }

        return true
    }

    return (DFS(roots[0]) && visited.every(v => v === true))
}



var BFSSolution = function(n, leftChild, rightChild){
    let inDegree = new Array(n).fill(0)

    for (let i = 0; i<n; i++){
        if (leftChild[i] != -1){
            inDegree[leftChild[i]] ++
        }

        if (rightChild[i] != -1){
            inDegree[rightChild[i]] ++
        }
    }


    let root = null;
    for (let i = 0; i<n; i++){
        if (inDegree[i] === 0){
            if (root === null){
                root = i
            }
            else {
                return false
            }
        }
    }

    if (root === null) return false

    let visited = new Array(n).fill(false)
    let queue = [root]

    while (queue.length){
        let cur = queue.shift()
        if (visited[cur] === true) return false

        visited[cur] = true

        if (leftChild[cur] != -1){
            queue.push(leftChild[cur])
        }

        if (rightChild[cur] != -1){
            queue.push(rightChild[cur])
        }
    }

    return visited.every(v => v === true)
}