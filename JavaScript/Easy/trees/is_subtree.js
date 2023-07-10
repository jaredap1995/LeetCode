/**
 * 
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 * 
 */

const TreeNode = (val, left, right) => {
    this.val = (val === undefined ? 0 : val)
    this.right = (right === undefined ? null : right)
    this.left = (left === undefined ? null : left)
}

var isSubTree = function(root, subRoot) {
    // Write helper function to check if equal (same as simpler tree problems done previously)
    var checkEqual = (root1, root2) => {
        if (root1 === null && root2 === null) {return true}
        else if (root1 === null || root2 === null) {return false}
        else if (root1.val !== root2.val) {return false}
        else {return checkEqual(root1.left, root2.left) && checkEqual(root1.right, root2.right)}
    }

    if (root === null) {return false}
    else if (checkEqual(root, subRoot)) {return true}
    else {return isSubTree(root.right, subRoot) || isSubTree(root.left, subRoot)}

}