function Node(val, neighbors) {
    this.val === undefined ? 0 : val;
    this.neighbors === undefined ? [] : neighbors;
}

/**
 * @param {Node}
 * @return {Node}
 */

var cloneGraph = function(node) {
    if (!node) {
        return null
    }

    let cloneDict = {}
    let q = []

    root = new Node(node.val, [])
    cloneDict[node.val] = root
    q.push(node)

    while (q.length) {
        cur = q.pop()
        curClone = cloneDict[cur.val]

        for (let neighbor of cur.neighbors) {
            if (!cloneDict[neighbor.val]) {
                newClone = new Node(neighbor.val, [])
                cloneDict[neighbor.val] = newClone
                q.push(neighbor)
            }

            curClone.neighbors.push(cloneDict[neighbor.val])
        }
    }

    return root

}