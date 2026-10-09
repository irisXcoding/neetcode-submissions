# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p&q larger: search in the right sub-tree
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # if smaller: search in the left sub-tree
        elif root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
            

        