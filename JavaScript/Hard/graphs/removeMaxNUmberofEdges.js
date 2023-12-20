var UF = class {
    constructor(n){
        this.parent = new Array(n).fill(0).map((_, idx) => idx)
        this.rank = new Array(n).fill(1)
        this.size = 1
    }

    find = (x) => {
        if (this.parent[x] != x){
            this.parent[x] = this.find(x)
        }
        return this.parent[x]
    }

    union = (x,y) => {
        let xset = this.find(x)
        let yset = this.find(y)

        if (xset === yset) return false

        if (this.rank[xset] < this.rank[yset]){
            this.parent[xset] = yset
        } else if ( this.rank[xset] > this.rank[yset]){
            this.parent[yset] = xset
        } else {
            this.parent[xset] = yset
            this.rank[xset] ++
        }

        this.size ++
        return true

    }
}

var maxNumEdgesToRemove = function(n, edges){
    let aliceUF = UF(n)
    let bobUF = UF(n)
    let ans = 0

    for (const [type, node1, node2] of edges){
        if (type === 3 && (!aliceUF.union(node1, node2) || !bobUF.union(node1, node2))) {
            ans ++
        }
    }

    for (const [type, node1, node2] of edges){
        if (type === 1 && !aliceUF.union(node1, node2)) ans ++
        if (type === 2 && bobUF.union(node1, node2)) ans ++
    }

    return (bobUF.size === n && aliceUF.size === n) ? ans : -1

}