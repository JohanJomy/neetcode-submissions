# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ''

        def dfs(root):
            nonlocal res
            res += str(root.val) if root else 'N'
            res += ','

            if root:
                dfs(root.left)
                dfs(root.right)
        

        dfs(root)
        # print(res)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        
        def dfs(indx):
            nonlocal nodes

            if nodes[indx] == "N":
                return [None, indx+1]
            elif nodes[indx]:
            # else:
                node = TreeNode(int(nodes[indx]))
            else:
                return
            
            t = dfs(indx+1)
            node.left = t[0]

            t = dfs(t[1])
            node.right = t[0]

            return [node, t[1]]
            
        
        dummy = TreeNode()
        dummy.left = dfs(0)[0]

        return dummy.left
            
