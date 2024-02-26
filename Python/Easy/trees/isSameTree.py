def solution(p,q):
    def dfs(root1, root2):
        if root1 is None and root2 is None: return True
        if root1 is not None and root2 is None: return False
        if root1 is None and root2 is not None: return False
        if root1.val != root2.val: return False

        if dfs(root1.left, root2.left) and dfs(root1.right, root2.right):
            return True
        else:
            return False
        
    return dfs(p,q)