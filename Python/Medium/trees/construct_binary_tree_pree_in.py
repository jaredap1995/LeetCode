"""
Given two integer arrays preorder and inorder where preorder is 
the preorder traversal of a binary tree and inorder is the inorder traversal 
of the same tree, construct and return the binary tree.
"""

class TreeNode (object):
    def __init__(self, val, left, right):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def buildTree(self, preorder, inorder):
        in_index_map = dict(map(reversed, enumerate(inorder)))

        def build_tree(pre_start, in_start, in_end):
            if in_start >= in_end: return None, pre_start

            root_val = preorder[pre_start]
            root_index = in_index_map[root_val]

            l_tree, pre_end = build_tree(pre_start+1, in_start, root_index)
            r_tree, pre_end = build_tree(pre_end, root_index+1, in_end)

            return TreeNode(root_val, l_tree, r_tree), pre_end

        return build_tree(0,0, len(inorder))[0]
    

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

solution = Solution()
print(solution.buildTree(preorder, inorder))