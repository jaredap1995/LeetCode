"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes 
along the longest path from the root node down to the farthest leaf node."""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1


        
"""Root is TreeNode object and we call the recursive function MaxDepth on both the left and right
attributes of the TreeNode object. We then determine the max between the left and right depth and add 1 to it for 
the original root node."""
