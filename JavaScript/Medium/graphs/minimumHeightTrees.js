/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees_BruteForceTLE = function(n, edges) {
    let graph = new Array(n).fill(0).map(() => [])
    for (const [n1, n2] of edges) {
        graph[n1].push(n2)
        graph[n2].push(n1)
    }
    
    // Store indexes
    let result = {}

    var DFS = (node, root, visited, height) => {
        if (visited.has(node)) return

        visited.add(node)

        for (const neighbor of graph[node]){
            if (!visited.has(neighbor)){
                new_height = height + 1;
                result[root] = Math.max(new_height, result[root]);
                console.log(root, new_height)
                DFS(neighbor, root, visited, new_height)
            }
        }
    }

    for (let i = 0; i<n; i++) {
        let visited = new Set();
        let height = 0;
        result[i] = 0

        DFS(i, i, visited, height)
    }
    
    console.log(result)

};


n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]


// Topoligical Sort, find leaves (nodes with only one connection) and work backwards by trimming leaves
var findMinHeightTrees = function(n, edges){
    if (n === 1) return [0]

    let graph = new Array(n).fill(0).map(() => [])
    let degree = new Array(n).fill(0)
    for (const [n1, n2] of edges){
        graph[n1].push(n2)
        graph[n2].push(n1)
        degree[n1] ++
        degree[n2] ++
    }

    let leaves = []
    for (let i = 0; i<n; i++){
        if (graph[i].length === 0){
            leaves.push(i)
        }
    }

    
    while (n > 2){
        n -= leaves.length
        let newLeaves = []
        for (leaf of leaves){
            for (neighbor of graph[leaf]){
                if (--degree[neighbor] === 1){
                    newLeaves.push(neighbor)
                }
            }
        }
        leaves = newLeaves
    }

    return leaves
}