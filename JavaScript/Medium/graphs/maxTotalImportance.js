var solution = function (n, roads) {
    let arr = new Array(n).fill(0)
    for (const [road1, road2] of roads) {
        arr[road1] ++
        arr[road2] ++
    }

    arr.sort((a,b) => a-b)
    let res = 0
    for (let i = 0; i<n; i++){
        res += arr[i] * (i+1)
    }

    return res
}