/**
 * @param {TreeNode} root
 * @return {number}
 *
 */


var TreeNode = (val, left, right) => {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

var maxPathSum = function (root) {
    let maxSum = -Infinity;
    var helper = function (node){
        if (node === null) {return 0}

        let left = Math.max((node.left, 0));
        let right = Math.max((node.right, 0));
        let total = node.val + left + right;
        maxSum = Math.max((total, maxSum))

        return node.val + Math.max((left, right))
    }
    helper(root)
    return maxSum
}