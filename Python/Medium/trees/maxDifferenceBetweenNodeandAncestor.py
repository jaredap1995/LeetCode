def solution (root):
    def dfs(node, high, low):
        if not node: return 0

        high = max(high, node.val)
        low = min(low, node.val)

        if not node.left and not node.right:
            return high - low
        
        return max(dfs(node.left ,high, low), dfs(node.right, high, low))
    

    return dfs(root, root.val, root.val)
