var solution = function(strs){
    let map = new Map();
    for (let str of strs){
        let k = str.splt('').sort().join('')
        if (!map[k]) map[k] = []
        map[k].push(str)
    }

    return Object.values(map)
}