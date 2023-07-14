


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        def helper(node, lower, upper):
            if not node: return True

            if lower is not None and node.val <= lower or upper is not None and node.val >=upper: return False

            if not helper(node.right, node.val, upper): return False
            if not helper(node.left, lower, node.val): return False

            return True
        
        return helper(root, None, None)