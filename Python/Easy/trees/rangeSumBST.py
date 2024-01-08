def solution(root, high, low):
    count = 0

    def dfs(node):
        nonlocal count
        if node is None: return 0

        if node.val >= low and node.val <= high:
            count += node.val

        if node.val < high:
            dfs(node.right)

        if node.val > low:
            dfs(node.left)

        return count
    
    return dfs(root)