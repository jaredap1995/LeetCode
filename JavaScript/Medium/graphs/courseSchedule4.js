var solution = function(numCourses, prerequisites, queries){
    let graph = new Array(numCourses).fill(0).map(() => [])
    let reachable = new Array(numCourses).fill(0).map(() => new Set())

    for (const [prereq, course] of prerequisites){
        graph[prereq].push(course)
    }

    var DFS = (node) => {
        if (reachable[node].size > 0){
            return reachable[node]
        }

        for (const neighbor of graph[node]){
            reachable[node].add(neighbor)
            for (const indirectNeigh of DFS(neighbor)){
                reachable[node].add(indirectNeigh)
            }
        }

        return reachable[node]
    }

    for (let i = 0; i< numCourses; i++){
        DFS(i)
    }

    output = []
    for (const [prereq, course] of queries){
        output.push(reachable[prereq].has(course))
    }

    return output
}

