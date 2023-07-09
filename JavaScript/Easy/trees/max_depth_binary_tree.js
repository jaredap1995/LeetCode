/**
 * @param {TreeNode} root
 * @return {boolean}
 */

const TreeNode = (val, left, right) => {
    this.val = (val === undefined ? 0: val)
    this.left = (left === undefined ? null: val)
    this.right = (right === undefined ? null: val)
}

var maxDepth = function (root){
    if (root == null){
        return 0
    } else {
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return Math.max(left, right) + 1
    }
}