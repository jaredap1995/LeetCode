var solution = function(equations) {
    let parents = {}
    let diff = []

    var find = (x) => {
        if (!parents.hasOwnProperty(x)) {
            return x}
        else {
            return find(parents[x])
        }
    }

    for (let eq of equations) {
        let a = eq[0]
        let b = eq[3]
        if (eq[1] === "="){
            let x = find(a)
            let y = find(b)
            if (x !== y) {
                parents[y] = x
            } else {
                diff.push([a,b])
            }
        }
    }

    for (const [a,b] of diff) {
        if (find(a) === find(b)) {
            return false
        }
    }

    return true
}