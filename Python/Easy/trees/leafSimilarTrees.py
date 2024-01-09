def solution(root1, root2):
    def dfs(node, leafs):
        if node == None: return

        if node.left is None and node.right is None:
            leafs.append(node.val)

        if node.left is not None:
            dfs(node.left, leafs)
        if node.right is not None:
            dfs(node.right, leafs)

        return leafs
    
    return dfs(root1, []) == dfs(root2, [])