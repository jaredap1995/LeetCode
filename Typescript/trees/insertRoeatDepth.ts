

 class TreeNode {
      val: number
      left: TreeNode | null
      right: TreeNode | null
      constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.left = (left===undefined ? null : left)
          this.right = (right===undefined ? null : right)
     }
 }

function addOneRow(root: TreeNode | null, val: number, depth: number): TreeNode | null {

    if (depth === 1){
        let new_root = new TreeNode(val)
        new_root.left = root
        return new_root
    }

    var dfs = (node: TreeNode, d: number): null => {
        if (!node) return null

        if (d === depth - 1){
            let leftNode = node.left
            let rightNode = node.right
            let l = new TreeNode(val, leftNode)
            let r = new TreeNode(val, null, rightNode)
            node.left = l
            node.right = r
        } else {
            if (node.left){
                dfs(node.left, d+1)
            }
            if (node.right){
                dfs(node.right, d+1)
            }
        }
    }

    dfs(root, 1)
    return root
};