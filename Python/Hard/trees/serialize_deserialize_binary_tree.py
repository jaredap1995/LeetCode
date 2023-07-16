"""

Serialization is the process of converting a data structure or object into a sequence of
 bits so that it can be stored in a file or memory buffer, or transmitted across a network
 connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on
 how your serialization/deserialization algorithm should work. You just need to ensure 
 that a binary tree can be serialized to a string and this string can be deserialized to 
 the original tree structure.

"""

class TreeNode(object):
    def __init__ (self, val, right, left):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def serialize(self, root):
        if not root:
            return '#'
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)

    # We do not need to str left and right because the recusive nature will make sure when
    #we reach the end for both we will return the str(root.val) and then work our way back up
        return str(root.val) + ',' + left + ',' + right
        
    def deserialize (self, data):
        tree_list = data.split(',')

        def traversal ():
            node = tree_list.pop(0)
            if node == '#':
                return None
            
            new_node = TreeNode(int(node))
            new_node.left = traversal()
            new_node.right = traversal()
            return new_node
        
        return traversal()



