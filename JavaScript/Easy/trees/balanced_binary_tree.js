/**
 * @param {TreeNode} root
 * @return {boolean}
 */

const TreeNode = (val, left, right) => {
    this.val = (val === undefined ? 0: val)
    this.left = (left === undefined ? null: left)
    this.right = (right === undefined ? null: right)
}


var isBalanced = function (root) {
    if (root == null) {return true}
    if (Height(root) == -1) {return false;}
    return true
}

var Height = function(root) {
    if (root == null) {return 0}
    let left = Height(root.left)
    let right = Height(root.right)
    if (left < 0 || right < 0 || Math.abs(left-right)>1) {
        return -1
    }
    return Math.max(left, right) + 1
}