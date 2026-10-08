# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def isSametree(self, node_1, node_2):
        if not node_1 and not node_2:
            return True
        if not node_1 or not node_2:
            return False
        if node_1.val != node_2.val:
            return False
        return self.isSametree(node_1.left, node_2.left) and self.isSametree(node_1.right, node_2.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # time: O(m*n) space: O(h1+h2)
        # compare every node with subroot
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if self.isSametree(root, subRoot):
            return True
        # move to the next node
        l_same = self.isSubtree(root.left, subRoot)
        if l_same:
            return True
        r_same = self.isSubtree(root.right, subRoot)
        if r_same:
            return True
        return False