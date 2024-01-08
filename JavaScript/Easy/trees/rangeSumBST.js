var solution = function(root, low, high){
    let count = 0

    var dfs = (node) => {
        if (node === null) return 0

        if (node.val >= low && node.val <= high){
            count += node.val
        }

        if (node.val < high){
            dfs(node.right)
        }
        if (node.val > low){
            dfs(node.left)
        }

        return count
    }

    return dfs(root)
}