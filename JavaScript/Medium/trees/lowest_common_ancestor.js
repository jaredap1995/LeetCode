/**
 * 
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 * 
 */

//Binary Search Tree Node != Binary Tree Node
const TreeNode = (val, left, right) => {
    this.val = val
    this.right = this.left = null
}

var lowestCommonAncestor = function (root, p, q) {
    if (p.val < root.val && q.val < root.val){
        return lowestCommonAncestor(root.left, p, q)
    }
    else if (p.val >root.val && q.val > root.val) {
        return lowestCommonAncestor (root.right)
    }
    else { return root }
}