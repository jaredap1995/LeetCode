var solution = function(n, edges){
    let indegree = {}
    for (let i = 0; i<n; i++){
        indegree[i] = 0
    }

    edges.array.forEach((_, n2) => {
        indegree[n2] ++       
    });

    let champ = []
    for (const [k,v] of Object.entries(indegree)){
        if (v === 0) champ.push(k)
    }

    return champ.length === 1 ? champ[0] : -1
}