/**
 * @param {TreeNode} root
 * @return {boolean}
 * 
 */

var TreeNode = (val, left, right) => {
    this.val = (val === undefined ? 0 : val)
    this.right = (right === undefined ? null : right)
    this.left = (left === undefined ? null : left)
}

var isValidBST = function (root) {
    var helper = function (node, lower, upper){
        if (!node) return true;

        if ((lower !== null && node.val <= lower) || (upper !==null && node.val >= upper)) return false;

        if (!helper(node.right, node.val, upper)) return false;
        if (!helper(node.left, lower, node.val)) return false;

        return true
    }
  
    return helper(root, null, null)
}