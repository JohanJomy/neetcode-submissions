"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}
        if not node:
            return None

        root = Node(node.val)

        def dfs(original, new):

            for n in original.neighbors:
                if n in hmap:
                    new.neighbors.append(hmap[n])
                else:
                    nd = Node(n.val)
                    hmap[n] = nd 
                    new.neighbors.append(nd)
                    dfs(n, nd)
        
        dfs(node, root)
        print(hmap)
        return root

        


