class TreeNode {
    val: number;
    right: TreeNode | null;
    left: TreeNode| null;
    constructor(val: number, left: TreeNode | null, right: TreeNode | null){
        this.val = (val === undefined ? 0 : val)
        this.right = (this.right === undefined ? null : right)
        this.left = (this.left === undefined ? null : left)
    }
}

var leftMostLeft = function(root: TreeNode): number {
    let leafs: [number, number] [] = []
    var dfs = (node: TreeNode | undefined, lvl: number): undefined => {
        if (node?.right === null && node.left === null) {
            leafs.push([node.val, lvl + 1])
            return
        }

        if (node?.left !== null) dfs(node?.left, lvl + 1)
        if (node?.right !== null) dfs(node?.right, lvl+1)
    }

    dfs(root, 0)
    let max_level: number = Math.max(...leafs.map((val) => val[1]))
    let max_leafs: [number, number][] = leafs.filter((val) => val[1] === max_level)
    return max_leafs[0][0]
}