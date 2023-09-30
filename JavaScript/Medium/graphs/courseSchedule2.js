var findOrder = function (numCourses, prerequisites) {
    let dic = new Array(numCourses).fill(0).map(() => [])

    for (const [course, pre] of prerequisites) {
        dic[course].push(pre)
    }

    let output = []
    let visit = new Set()
    let cycle = new Set()

    var dfs = (course) => {
        if (cycle.has(course)){
            return false
        }
        if (visit.has(course)){
            return true
        }
        cycle.add(course)

        for (let pre of dic[course]){
            if (!dfs(pre)){
                return false
            }
        }
        cycle.delete(course)
        visit.add(course)
        output.push(course)
        return true
    }

    for (let i = 0; i< numCourses; i++) {
        if (!dfs(i)){
            return []
        }
    }
    return output
}