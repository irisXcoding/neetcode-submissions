# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l, r):
            if not node:
                return True
            if node.val<=l or node.val>=r:
                return False
            if not dfs(node.left, l, min(node.val, r)):
                return False
            if not dfs(node.right, max(node.val, l), r):
                return False
            return True
        
        return dfs(root, -1000000001, 1000000001)