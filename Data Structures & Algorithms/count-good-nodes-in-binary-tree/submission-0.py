# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        # self.res = []
        self.ctr = 0
        self.maxval = []

    def goodNodes(self, root: TreeNode) -> int:

        self.dfs(root)

        return self.ctr
        
    def dfs(self, root):
        if root == None:
            return

        if not self.maxval:
            self.maxval.append(root.val)
        else:
            mx = self.maxval[-1] if self.maxval[-1] > root.val else root.val
            self.maxval.append(mx)
        
        if root.val >= self.maxval[-1]:
            # self.res.append(root.val)
            self.ctr += 1

        self.dfs(root.left)
        self.dfs(root.right)

        self.maxval.pop()
    