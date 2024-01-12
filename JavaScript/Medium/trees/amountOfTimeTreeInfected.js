var solution = (root, start) => {
    var adjList = (node) => {
        let graph = {}
        let queue = [root]

        while (root.length){
            let cur = queue.shift()

            if (!graph[cur.val]) graph[cur.val] = []

            if (cur.left !== null && cur.right !== null){
                if (!graph[cur.left.val]) graph[cur.left.val] = []
                if (!graph[cur.right.val]) graph[cur.right.val] = []
                graph[cur.val].push(cur.right.val)
                graph[cur.val].push(cur.left.val)
                graph[cur.right.val].push(cur.val)
                graph[cur.left.val].push(cur.val)
                queue.push(cur.left)
                queue.push(cur.right)
            } else if (cur.left !== null && cur.right === null) {
                if (!graph[cur.left.val]) graph[cur.left.val] = []
                graph[cur.val].push(cur.left.val)
                graph[cur.left.val].push(cur.val)
                queue.push(cur.left)
            } else if (cur.left === null && cur.right !== null){
                if (!graph[cur.right.val]) graph[cur.right.val] = []
                graph[cur.val].push(cur.right.val)
                graph[cur.right.val].push(cur.val)
                queue.push(cur.right)
            }
        }
    }

    graph = adjList(root)

    let queue = [start]
    let visited = new Set()
    visited.add(start)
    let dist = 0
    
    while (queue.length){
        dist ++
        let n = queue.length
        for (let i = 0; i<n; i++ ){
            let cur = queue.shift()
            visited.add(cur)
            for (const neighbor of graph[cur]){
                if (!visited.has(neighbor)){
                    queue.push(neighbor)
                }
            }
        }
    }

    return dist - 1 > 0 ? dist  - 1 : 0
}