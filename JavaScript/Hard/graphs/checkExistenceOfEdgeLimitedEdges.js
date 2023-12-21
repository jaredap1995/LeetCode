var UF = class {
    constructor(n){
        this.parent = new Array(n).fill(0).map((_, idx) => idx)
        this.rank = new Array(n).fill(1)
    }

    find = (x) => {
        if (this.parent[x] != x) {
            this.parent[x] = this.find(this.parent[x])
        }
        return this.parent[x]
    }

    union = (x,y) => {
        let xset = this.find(x)
        let yset = this.find(y)

        if (xset === yset) return

        if (this.rank[xset] < this.rank[yset]){
            this.parent[xset] = yset
        } else if (this.rank[xset] > this.rank[yset]){
            this.parent[yset] = xset
        } else {
            this.parent[xset] = yset
            this.rank[xset] ++
        }
    }
}

var solution = function(n, edgeList, queries){
    // sort the edgeList
    edgeList.sort((a,b) => a[2]-b[2])
    // add the index to the queries
    queries = queries.map((arr, idx, _) => [idx, arr]);
    // sort the queries
    queries.sort((a,b) => a[1][2] - b[1][2])
    // create result
    let res = new Array(n).fill(null)

    uf = new UF(n)
    idx = 0
    // iterate over the queries sorted by limit
    for (let [i, [n1, n2, limit]] of queries){
        while (idx < edgeList.length && edgeList[2] < limit){
            uf.union(edgeList[idx][0], edgeList[idx][1])
            idx ++
        }

        res[i] = (uf.find(n1) === uf.find(n2))
    }

    return res
}

n = 5
edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]]
queries = [[0,4,14],[1,4,13]]

console.log(solution(n, edgeList, queries))