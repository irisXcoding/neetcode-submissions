# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # get the root from preorder, split left&right from inorder
        map_dict = {}
        n = len(preorder)
        for idx, val in enumerate(inorder):
            map_dict[val] = idx
        def dfs(start, end):
            if start>end or self.root_idx>n-1:
                return None
            root_val = preorder[self.root_idx]
            inoder_idx = map_dict[root_val]
            node = TreeNode(root_val)
            self.root_idx+=1
            node.left = dfs(start, inoder_idx-1)
            node.right = dfs(inoder_idx+1, end)
            return node
        self.root_idx = 0
        return dfs(0, len(inorder)-1)

        