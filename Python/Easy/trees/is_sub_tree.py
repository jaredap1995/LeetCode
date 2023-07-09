"""

Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same 
structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in
tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of 
itself.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        def checkEqual(root, subroot):
            if root is None and subroot is None:
                return True
            elif root is None or subroot is None:
                return False
            elif root.val != subroot.val:
                return False
            else:
                return checkEqual(root.left, subroot.left) and checkEqual(root.right, subroot.right)
            
        if root is None:
            return False
        elif root == subRoot:
            return True
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
