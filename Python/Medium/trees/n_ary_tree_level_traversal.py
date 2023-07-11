"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

"""


"""Another BFS problem but need to use extend instead of append duie to children being a list"""

class Node(object):
    def __init__(self, val= None, children = None):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return
        
        queue = []
        solution = []
        queue.append(root)

        while len(queue) > 0:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)

                if node.children is not None:
                    queue.extend(node.children)
                
            solution.append(temp)

        return solution