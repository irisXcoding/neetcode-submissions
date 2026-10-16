# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_len = -10001
        def dfs(node):
            if not node:
                return 0
            left_len = max(dfs(node.left), 0)
            right_len = max(dfs(node.right), 0)
            self.max_len = max(self.max_len, node.val+left_len+right_len)
            return node.val+max(left_len, right_len)
        dfs(root)
        return self.max_len