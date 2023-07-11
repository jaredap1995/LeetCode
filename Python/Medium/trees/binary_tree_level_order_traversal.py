""""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

"""

"""Solution: Implement a BFS using a queue, make sure to append values at each level to temporary list and append that list to solution"""


class TreeNode (object):
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left


class Solution(object):
    def levelOrder (self, root):
        if root is None:
            return 
        
        queue = []
        solution = []
        queue.append(root)

        while len(queue) > 0:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            solution.append(queue)

        return solution
