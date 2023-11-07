var solution = function(n, paths){
    let graph = new Array(n).fill(0).map(() => [])
    for (const [n1,n2] of paths){
        graph[n1].push(n2)
        graph[n2].push(n1)
    }

    let ans = new Array(n).fill(0)

    var setPop = (set) => {
        for (const value of set){
            set.delete(value)
            return value
        }
    }

    for (let i = 1; i<n+1;i++){
        let available = new Set([1,2,3,4])
        for (const neighbor of graph[i]){
            if (available.has(ans[neighbor-1])){
                available.delete(ans[neighbor-1])
            }
        ans[i-1] = setPop(available)
        }
    }

    return ans
}