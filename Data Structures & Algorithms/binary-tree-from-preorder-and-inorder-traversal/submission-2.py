# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        def build(start, end):
            while start == end:
                return
            val = preorder[self.count]
            node = TreeNode(val)
            i = val_idx_map.get(val)
            self.count += 1
            node.left = build(start, i)
            node.right = build(i+1, end)
            return node
        self.count = 0
        val_idx_map = {}
        for idx, val in enumerate(inorder):
            val_idx_map[val] = idx
        return build(0, len(inorder))


