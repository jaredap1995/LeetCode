/**
 * 
 * @param {TreeNode} root
 * @return {number[]}
 * 
 */


var TreeNode = function (val, left, right){
    this.val = (val === undefined ? 0: val)
    this.right = (right === undefined ? null : right)
    this.left = (left === undefined ? null : left)
}

var rightSideView = (root) => {
    if (!root) return [];

    let queue = [root];
    let solution = []

    while (queue.length > 0) {
        levelLength = queue.length
        for (let i = 0; i < levelLength; i++){
            let node = queue.shift();
            if (node.left) {queue.push(node.left)}
            if (node.right) {queue.push(node.right)}
            if (i === queue.length -1) {solution.push(node.val)}
    }
    return solution
}}
