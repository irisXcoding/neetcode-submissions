# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        # 1. BFS search
        q = deque([root])
        layer_count = 1  # len(q)
        # 2. append the last item to final res
        while q:
            item = q.popleft()
            if layer_count ==1:
                res.append(item.val)
            layer_count -= 1
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)
            if layer_count == 0:
                layer_count = len(q)
        return res
