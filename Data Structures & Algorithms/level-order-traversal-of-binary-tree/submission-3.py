# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        count = 1
        res, sub_list = [], []
        while dq:
            if count ==0:
                count = len(dq)
                res.append(sub_list)
                sub_list = []
            node = dq.popleft()
            count -= 1
            sub_list.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        if sub_list:
            res.append(sub_list)
        return res




        