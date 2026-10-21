# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -1001
        def dfs(node):
            if not node:
                return 0
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            self.max_sum = max(self.max_sum, node.val+left_max+right_max)
            return max(left_max, right_max)+node.val
        dfs(root)
        return self.max_sum