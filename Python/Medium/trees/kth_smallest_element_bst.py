
"""

Given the root of a binary search tree, 
and an integer k, return the kth smallest value (1-indexed) 
of all the values of the nodes in the tree.

"""




class TreeNode (object):
    def __init__(self, val, left, right):
        self.val = val
        self.right = right
        self.left = left

class Solution(object):
    def kthSmallest(self, root, k):
        values = []
        def inOrder (node):
            nonlocal values
            if node is not None:
                # values.append(node.val) Pre-order traversal
                inOrder(node.left)
                values.append(node.val) # In-order traversal---this is the solution
                inOrder(node.right)
                # values.append(node.val) Post-order traversal
            else: return
        inOrder(root)
        return values[k-1], values

root = TreeNode(3, TreeNode(1, None, TreeNode(2, None, None)), TreeNode(4, None, None))
k = 1

solution = Solution()
print(solution.kthSmallest(root, k))


