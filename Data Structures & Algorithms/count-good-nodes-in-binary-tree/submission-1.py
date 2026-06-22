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

    def goodNodes(self, root: TreeNode) -> int:

        self.dfs(root, root.val)

        return self.ctr
        
    def dfs(self, root, maxval):
        if root == None:
            return

        mx = maxval if maxval > root.val else root.val
        
        if root.val >= maxval:
            self.ctr += 1

        self.dfs(root.left, mx)
        self.dfs(root.right, mx)

    