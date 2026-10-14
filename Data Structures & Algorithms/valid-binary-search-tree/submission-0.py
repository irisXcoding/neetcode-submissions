# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, _min, _max):
            if not node:
                return True
            if not (node.val>_min and node.val<_max):
                return False
            if not dfs(node.left, _min, min(_max, node.val)):
                return False
            if not dfs(node.right, max(_min, node.val), _max):
                return False
            return True

        return dfs(root, -1000000001, 1000000000)