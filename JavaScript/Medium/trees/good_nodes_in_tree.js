/**
 * @param {TreeNode} root
 * @return {number} 
 */

var TreeNode = (root,  left, right) => {
    this.val = (val === undefined ? 0 : val)
    this.right = (right === undefined ? null : right)
    this.left = (left === undefined ? null : left)
}

var goodNodes = function (root) {
    good = 0
    max_ = root.val
    var dfs = (root) => {
        if (!root.val) {return}
        left_max = dfs(root.left)
        right_max = dfs(root.right)
        if (root.val < max_) {return}
        else {good ++}
        return
    }
}