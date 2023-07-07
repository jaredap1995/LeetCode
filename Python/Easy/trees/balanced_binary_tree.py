"""

Given a binary tree, determine if it is 
height-balanced.

height-balanced: A height-balanced binary tree is a 
binary tree in which the depth of the two subtrees 
of every node never differs by more than one.

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
       return self.Height(root >=0)
    def Height(self, root):
        if not root: return 0
        left = self.Height(root.left)
        right = self.Height(root.right)
        if left < 0 or right < 0 or abs(right-left)>1: return -1
        return max(left, right) + 1


        
