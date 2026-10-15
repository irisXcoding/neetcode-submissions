# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.map_idx = {}
        for idx, val in enumerate(inorder):
            self.map_idx[val] = idx
        self.pre_idx = 0
        def dfs(start, end):
            if start==end:
                return
            node_val = preorder[self.pre_idx]
            self.pre_idx+=1
            node = TreeNode(node_val)
            in_idx = self.map_idx[node_val]
            node.left = dfs(start,in_idx)
            node.right = dfs(in_idx+1, end)
            return node

        root = dfs(0, len(inorder))
        return root
        