var solution = function(root1, root2){
    var dfs = (node, leafs) => {
        if (node === null) return

        if (node.left === nul && node.right === null) {
            leafs.push(node.val)
        }

        if (node.right !== null) {
            dfs(node.right, leafs)
        }
        if (node.left !== null){
            dfs(node.left, leafs)
        }

        return leafs
    }

    return (JSON.stringify(dfs(root1, []))===JSON.stringify(dfs(root2, [])))
}