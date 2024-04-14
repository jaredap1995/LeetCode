def solution(root):
    res = 0
    def dfs(root, isLeft):
        nonlocal res
        if root is None: return

        if root.left is None and root.right is None:
            if isLeft:
                res += root.val

        dfs(root.left, True)
        dfs(root.right, False)

        return res
    
    return dfs(root, False)



