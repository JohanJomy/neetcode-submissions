# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root] if root else []
        res = []
        while q:
            newq = []
            last = None
            for i in q:
                last = i.val
                if i.left: newq.append(i.left)
                if i.right: newq.append(i.right)
            res.append(last)
            q = newq
        return res