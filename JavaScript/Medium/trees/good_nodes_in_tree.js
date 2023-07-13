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
        if (!root) {return}

        if (root.val >= max_){
            good++
            max_ = root.val
        }

        dfs(root.left)
        dfs(root.right)
    }
    dfs(root, max_)
    return good
}