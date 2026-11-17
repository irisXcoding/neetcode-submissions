# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.idx = 0
        def dfs(node):
            if not node:
                return
            res_left = dfs(node.left)
            if res_left is not None:
                return res_left
            self.idx+=1
            if self.idx==k:
                return node.val
            res_right = dfs(node.right)
            if res_right is not None:
                return res_right
 
        return dfs(root)
