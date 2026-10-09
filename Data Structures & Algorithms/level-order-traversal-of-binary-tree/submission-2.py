# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, sub_res = [], []
        queue = [root]
        layer_count = 1 # len(queue)
        while queue:
            if not layer_count:
               layer_count = len(queue)
               res.append(sub_res)
               sub_res = []
            parent_node = queue.pop(0)
            layer_count -= 1
            sub_res.append(parent_node.val)
            if parent_node.left:
                queue.append(parent_node.left)
            if parent_node.right:
                queue.append(parent_node.right)
        res.append(sub_res)
        return res
