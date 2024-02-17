var solution = function(arr, k) {
    let u = new Set(arr)
    var Counter = (arr) => {
        let dict = {}
        for (let i = 0; i< arr.length; i++){
            dict[arr[i]] = (dict[arr[i]] || 0) + 1
        }

        return dict
    }

    let c = Counter(arr)
    let keys = Object.keys(c).sort((a, b) => c[a] - c[b])

    for (const key of keys){
        while (c[key] > 0 && k >=1){
            c[key] --
            k --
            if (c[key] === 0){
                u.delete(Number(key))
            }
        }
    }

    return u.size
}