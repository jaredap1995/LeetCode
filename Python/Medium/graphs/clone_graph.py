class Node(object):
    def __init__(self, val=0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        clone_dict = {}
        queue = []

        rootClone = Node(node.val, [])
        clone_dict[node.val] = rootClone
        queue.append(node)

        while queue:
            cur = queue.pop()
            curClone = clone_dict[cur.val]

            for neighbor in cur.neighbors:
                if neighbor.val not in clone_dict:
                    newClone = Node(neighbor.val, [])
                    clone_dict[neighbor.val] = newClone
                    queue.append(neighbor)

            curClone.neighbors.append(clone_dict[neighbor.val]) 

        return rootClone