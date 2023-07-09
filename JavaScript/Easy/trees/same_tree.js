/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */

const TreeNode = (val, left, right) => {
    self.val = (val === undefined ? 0 : val)
    self.left = (left === undefined ? null : left)
    self.right = (right === undefined ? null: right)
}

var isSame = function (tree1,tree2) {
    let output = true;
    const dfs = function (tree1, tree2){
        if (tree1?.val !== tree2?.val) {
            return output = false;
        } //base case

        // left (check both are not undefined)...recursive -> tree1 is value and tree 2 is not, tree2 is value and tree 1 is not

        //the question mark operators allow a 'null' value to be converted to an undefined

        if (tree1?.left !== undefined && tree2?.left !==undefined){  //they both have values-->recurse
            dfs(tree1?.left, tree2?.left)
        } 
        else if (!tree1?.left && tree2?.left) {return output = false}
        else if (tree1?.left && !tree2?.left) {return output = false}

        // repeat same logic for right

        if (tree1?.right !== undefined && tree2?.right !== undefined){
            dfs(tree1?.right, tree2?.right)
        }
        else if (!tree1?.right && tree2?.right) {return output = false}
        else if (tree1?.right && !tree2?.right) {return output = false}
    }

    dfs(tree1,tree2);
    return output
}

