var solution = (s, t) => {
    let cs = {}
    let ct = {}

    for (let i = 0; i< s.length; i++){
        if (!cs[s[i]]) cs[s[i]] = 0
        if (!ct[t[i]]) ct[t[i]] = 0
        cs[s[i]]++
        ct[t[i]] ++
    }

    let res = 0
    for (const [k, v] of Object.entries(cs)){
        if (cs[k] > ct[k]){
            res += cs[k]-ct[k]
        } else if (cs[k] > 0 && !ct[k]){
            res += cs[k]
        }
    }

    return res
}