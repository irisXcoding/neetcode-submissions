# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, cnt):
        if not node:
            self.max_d = max(self.max_d, cnt)
            return
        self.dfs(node.left, cnt+1)
        self.dfs(node.right, cnt+1)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        self.dfs(root, 0)
        return self.max_d
        