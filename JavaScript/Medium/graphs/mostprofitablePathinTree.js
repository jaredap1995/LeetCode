/**
 * @param {number[][]} edges
 * @param {number} bob
 * @param {number[]} amount
 * @return {number}
 */
var mostProfitablePath__Incorrect = function (edges, bob, amount) {
    let n = amount.length
    let graph = new Array(n).fill(0).map(() => [])

    for (const [n1, n2] of edges) {
        graph[n1].push(n2)
        graph[n2].push(n1)
    }

    var DFS = (node, parent, path) => {
        if (node === 0) {
            return path
        }

        for (const neighbor of graph[node]) {
            if (neighbor === parent) {
                continue
            }
            path.push(neighbor)
            let result = DFS(neighbor, node, path)
            if (result !== undefined && result !== false) {
                return result
            }
            path.pop()
        }
        return false
    }

    let bob_path = DFS(bob, -1, [bob])
    let step = {}
    for (let i = 0; i < bob_path.length; i++) {
        step[bob_path[i]] = i
    }

    let ans = -Infinity
    let ini_profit = bob_path[0] === 0 ? Math.floor(amount[0] / 2) : amount[0]
    let depth = 0
    let queue = [[0, -1, ini_profit]]

    while (queue.length) {
        for (let j = 0; j < queue.length; j++) {
            let [cur, parent, profit] = queue.shift()

            if (graph[cur].length === 1 && cur != 0) {
                ans = Math.max(profit, ans)
            }

            for (const neighbor of graph[cur]) {
                if (neighbor === parent) continue

                let new_profit
                if (!step.hasOwnProperty(neighbor) || depth + 1 < step[neighbor]) {
                    new_profit = amount[neighbor]
                }
                else if (depth + 1 === step[neighbor]) {
                    new_profit = Math.floor(amount[neighbor] / 2)
                } else {
                    new_profit = 0
                }
                queue.push([neighbor, cur, new_profit + profit])
            }
        }
        depth++
    }

    return ans
};

var correctSolution = function(edges, bob, amount){
    let n = amount.length
    let graph = new Array(n).fill(0).map(() => [])

    for (const [n1,n2] of edges){
        graph[n1].push(n2)
        graph[n2].push(n1)
    }

    var DFS = (node, parent, time) => {
        let totalBob = node == bob ? 0: Infinity
        let newScore = -Infinity

        for (const neighbor of graph[node]){
            if (neighbor === parent) continue

            const [score, bobTime] = DFS(neighbor, node, time +1)
            totalBob = Math.min(totalBob, bobTime)
            newScore = Math.max(score, newScore)
        }

        if (newScore === -Infinity) newScore = 0
        if (time < totalBob) newScore += amount[node]
        else if (time === bobTime) newScore += amount[node] /2

        return [newScore, totalBob]
    }

    return DFS(0,-1,0)[0]
}