var solution = (root) => {
    var dfs = (node, high, low) => {
        if (!node) return 0

        high = Math.max(node.val, high)
        low = Math.min(node.val, low)

        if (node.left === null && node.right === null){
            return high - low
        }

        return Math.max(dfs(node.right, high, low), dfs(node.left, high, low))
    }

    return dfs(root, root.val, root.val)
}
