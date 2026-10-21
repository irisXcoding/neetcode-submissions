# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node, _max):
            if not node:
                return
            if node.val>=_max:
                self.count+=1
            dfs(node.left, max(_max, node.val))
            dfs(node.right, max(_max, node.val))
        dfs(root, -101)
        return self.count