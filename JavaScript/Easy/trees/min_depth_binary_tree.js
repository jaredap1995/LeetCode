/**
 * 
 * @param {TreeNode} root
 * @return {number}
 * 
 */

const TreeNode = (val, left, right) => {
    this.val = (val === undefined ? 0 : val)
    this.left (left === undefined ? null : left)
    this.right (right === undefined ? null : right)
}

var minDepth = (root) => {
    if (root == null) {
        return 0
    } else {
        let left = minDepth (root.left)
        let right = minDepth (root.right)
        if (root.right == null && root.left == null){
            return 1
        }
        if (root.right == null){
            return 1 + left
        }
        if (root.left == null) {
            return 1 + right
        }
        return Math.min(left,right) + 1
    }
}