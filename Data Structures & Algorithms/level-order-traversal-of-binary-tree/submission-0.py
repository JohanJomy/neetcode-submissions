# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [root] if root else []
        res = []
        while q:
            new_q = []
            level = []
            for i in q:
                level.append(i.val)
                if i.left: new_q.append(i.left)
                if i.right: new_q.append(i.right)
            res.append(level)
            q = new_q
        
        return res
