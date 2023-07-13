"""
Given the root of a binary tree, 
imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

root = [1,2,3,null,5,null,4]
[1,3,4]
"""

"""Notes:

We need to know level of object, and the right most node on eahc level.
Right most can be left node if there are no right nodes covering it up
"""

class TreeNode(object):
    def __init__(self, val, right, left):
        self.val = val
        self.right = right
        self.left = left

class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return
        
        queue = []
        solution = []
        queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            solution.append(node.val)

        return solution
    
root = TreeNode(1, TreeNode(2, None, TreeNode(5, None, None)), TreeNode(3, None, TreeNode(4, None, None)))
print(Solution().rightSideView(root))