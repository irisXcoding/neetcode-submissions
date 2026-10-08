# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node_1, node_2, is_same):
        if not is_same:
            return None, None, False
        if not node_1 and not node_2:
            return None, None, True
        if not node_1 or not node_2:
            return None, None, False
        if node_1.val != node_2.val:
            return None, None, False
        l_1, l_2, l_same = self.dfs(node_1.left, node_2.left, True)
        if not l_same:
            return None, None, False
        r_1, r_2, r_same = self.dfs(node_1.right, node_2.right, True)
        if not r_same:
            return None, None, False
        return None, None, True


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        _, _, is_same = self.dfs(p, q, True)
        return is_same
            