class TreeNode{
    val: Number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: Number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}
var solution = function(root: TreeNode): Number {
    let ans = 0
    var dfs = (root: TreeNode | null): number => {
        if (root === null) return 0
        let l = dfs(root.left)
        let r = dfs(root.right)
        ans = Math.max(ans, Number(l) + Number(r))
        return 1 + Math.max(l, r)
    }

    dfs(root)
    return ans
}