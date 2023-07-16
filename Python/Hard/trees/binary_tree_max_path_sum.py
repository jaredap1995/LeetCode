"""

A path in a binary tree is a sequence of nodes where each pair of 
adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

"""

import math

class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.right = right
        self.left = left

class Solution (object):
    def maxPathSum(self, root):
        max_sum = float('-inf') #Stores max path so far
        def helper(node):
            nonlocal max_sum
            if node is None: return 0

            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            total = node.val + left + right
            max_sum = max(max_sum, total)

            return node.val + max(left, right)
        helper(root)

        return max_sum
