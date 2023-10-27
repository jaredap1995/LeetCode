var loudAndRich = function (richer, quiet) {
    let n = quiet.length
    let richer_count = new Array(n).fill(0)
    let graph = new Array(n).fill(0).map(() => [])
    let answer = []
    for (let i = 0; i<n; i++){answer.push(i)}

    for (const [rich,poor] of richer){
        graph[rich].push(poor)
        richer_count[poor] ++
    }

    let queue = []
    for (let i = 0; i<n; i++){
        if (richer_count[i]===0){
            queue.push(i)
        }
    }

    while (queue.length) {
        let cur = queue.shift()
        for (const neighbor of graph[cur]){
            if (quiet[answer[neighbor]] > quiet[answer[cur]])
            richer_count[neighbor] --
            if (richer_count[neighbor] === 0) {
                queue.push(neighbor)
            }
        }
    }

    return answer

}