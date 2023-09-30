var canFinish = function (numCourses, preRequisities) {
    const graph = new Array(numCourses).fill(0).map(() => [])

    for (const [course, pre] of preRequisities) {
        graph[course].push(pre)
    }

    const visited = new Array(numCourses).fill(0)

    var DFS = (course) => {
        if (visited[course]==1) {return true}
        if (visited[course]==2) {return false}

        visited[course] = 1

        for (const pre of graph[course]) {
            if (DFS(pre)) {return true}
        }

        visited[course]=2
        return false
    }

    for (let i = 0; i<numCourses; i++) {
        if (DFS(i)) {return false}
    }

    return true
}