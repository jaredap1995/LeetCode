# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(0, root)]
        g = collections.defaultdict(list)
        while queue:
            lvl, cur = queue.pop(0)
            val = cur.val

            # if cur.left is None and cur.right is None and not queue: return True

            #root logic
            if lvl == 0:
                if val % 2 == 0:
                    return False

            #Even condition logic
            elif lvl % 2 == 0:
                if val % 2 == 0:
                    return False

                if len(g[lvl]) == 0:
                    g[lvl].append(val)
                else:
                    if val > g[lvl][-1]:
                        g[lvl].append(val)
                    else: 
                        return False
            
            # Odd Logic
            elif lvl % 2 != 0:
                if val % 2 != 0:
                    return False

                if len(g[lvl]) == 0:
                    g[lvl].append(val)
                else:
                    if val < g[lvl][-1]:
                        g[lvl].append(val)
                    else:
                        return False

            if cur.left is not None:
                queue.append((lvl + 1, cur.left))
            if cur.right is not None:
                queue.append((lvl + 1, cur.right))



        return True


