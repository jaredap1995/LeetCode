var solution = function(word1, word2){
    if (word1.length !== word2.length) return false

    var eqSet = (xs, ys) => {
        let s1 = new Set(xs), s2 = new Set(ys)
        return s1.size === s2.size && [...s1].every((e) => s2.has(e))
    }

    if (!eqSet(word1, word2)) return false

    let c1 = {}, c2 = {}
    for (const c of word1){
        c1[c] = (c1[c] || 0) + 1
    }
    for (const c of word2) {
        c2[c] = (c2[c] || 0) +1
    }

    c1 = Object.values(c1).sort((a,b) => a-b)
    c2 = Object.values(c2).sort((a,b) => a-b)

    return c1.every((e,i) => e === c2[i])

}