"""
Given the roots of two binary trees p and q, 
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.

"""



def TreeNode (self, val, left, right):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
    def isSameTree (self, tree1, tree2):
        output = True
        def dfs(tree1, tree2):
            # Base Case
            nonlocal output

            if tree1 is None and tree2 is None:
                return 

            elif tree1 is None or tree2 is None:
                output = False
                return
            
            elif tree1.val != tree2.val:
                output = False
                return
            
            # Check left values for both trees, if not null, recurse, 
            # then check each tree to make sure equivalent, return False
            if tree1.left is not None and tree2.left is not None:
                dfs(tree1.left, tree2.left)
            elif bool(tree1.left) != bool(tree2.left):
                output = False
                return
            
            if tree1.right is not None and tree2.right is not None:
                dfs(tree1.right, tree2.right)
            elif bool(tree1.right) != bool(tree2.right): #We need bool to compare if one is None and the other is not None, not compare if they are the same (which is what happens without bool)
                output = False
                return output
            
        dfs(tree1, tree2)
        return output
            
