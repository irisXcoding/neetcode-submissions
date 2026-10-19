# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, _left, _right):
            if not node:
                return True
            if node.val <= _left or node.val >= _right:
                return False
            return dfs(node.left, _left, node.val) and dfs(node.right, node.val, _right)
        return dfs(root, -1000000001, 1000000001)
