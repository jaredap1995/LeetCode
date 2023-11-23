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
        for (let j = queue.length; j > 0; j--) {
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

edges = [[0,38],[0,59],[1,30],[1,62],[1,53],[2,41],[2,37],[3,21],[4,35],[4,54],[5,32],[5,69],[6,26],[6,16],[6,61],[6,52],[7,34],[8,10],[9,11],[9,43],[10,48],[11,29],[12,63],[12,58],[12,13],[13,36],[13,34],[14,65],[14,15],[15,17],[15,49],[16,40],[17,20],[17,24],[18,58],[19,25],[21,34],[22,55],[23,45],[23,59],[25,43],[27,32],[28,49],[28,33],[31,61],[33,39],[33,51],[33,53],[34,68],[34,69],[37,52],[42,52],[43,61],[44,58],[46,49],[47,55],[47,50],[48,56],[48,66],[50,58],[52,66],[52,65],[53,57],[54,63],[55,57],[59,60],[59,67],[59,65],[64,69]]

bob = 47
amount = [4664,5822,-9152,7258,-5468,4698,2568,9880,-4046,9884,-3540,-2260,5264,-7050,-6998,-1688,-6256,-5350,5136,7476,-4108,1288,1336,-6126,2940,698,-2900,-2342,-2310,858,572,640,-9674,5746,5068,7128,636,6680,-1840,3574,7592,-5882,-1974,-2766,-620,1088,-8930,7756,9966,380,8884,-954,-8198,-5862,-3100,7728,7090,-4648,4076,994,4232,9810,-2904,-1106,-4172,-5884,-9582,5320,-4086,6346]

console.log(mostProfitablePath__Incorrect(edges, bob, amount))

// var correctSolution = function(edges, bob, amount){
//     let n = amount.length
//     let graph = new Array(n).fill(0).map(() => [])

//     for (const [n1,n2] of edges){
//         graph[n1].push(n2)
//         graph[n2].push(n1)
//     }

//     var DFS = (node, parent, time) => {
//         let totalBob = node == bob ? 0: Infinity
//         let newScore = -Infinity

//         for (const neighbor of graph[node]){
//             if (neighbor === parent) continue

//             const [score, bobTime] = DFS(neighbor, node, time +1)
//             totalBob = Math.min(totalBob, bobTime)
//             newScore = Math.max(score, newScore)
//         }

//         if (newScore === -Infinity) newScore = 0
//         if (time < totalBob) newScore += amount[node]
//         else if (time === bobTime) newScore += amount[node] /2

//         return [newScore, totalBob]
//     }

//     return DFS(0,-1,0)[0]
// }