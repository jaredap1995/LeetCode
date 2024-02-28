def solution(root):
    leafs = []
    def dfs(node, lvl):
        nonlocal leafs
        if node.left is None and node.right is None:
            leafs.append((node.val, lvl))

        if node.left is not None:
            dfs(node.left)
        if node.right is not None:
            dfs(node.right)

    dfs(root)
    max_level = max([i[1] for i in leafs])
    max_leafs = filter(lambda x: x[1] == max_level, leafs)
    return max_leafs[0][0]
