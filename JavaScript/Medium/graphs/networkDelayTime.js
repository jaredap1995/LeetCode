var Solution = function (n, k, times){
    let graph = new Array(n+1).fill(0).map(() => [])
    for (const [n1,n2,time] of times){
        graph[n1].push([n2,time])
    }

    let minTimes = new Array(n+1).fill(Infinity)
    minTimes[k] = 0

    // [time, node]
    let queue = [[0,k]]

    while (queue.length) {
        let [curTime, curNode] = queue.shift() 
        if (graph[curNode]){
            if (curTime > minTimes[curNode]) continue
            for (const[neighbor, neighborTime] of graph[curNode]){
                let newTime = curTime + neighborTime
                if (newTime < minTimes[neighbor]){
                    minTimes[neighbor] = newTime
                    queue.push(neighbor)
                }
            }
        }
    }

    maxTime = Math.max(...minTimes.slice(1))
    if (maxTime === Infinity){
        return -1
    } else {
        return maxTime
    }
}