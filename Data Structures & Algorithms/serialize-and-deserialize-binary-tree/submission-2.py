# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # use the N as the empty node of the leaf node
        # time: O(n) space: O(n)
        res_list = []
        def dfs(node):
            if not node:
                res_list.append("N")
                return
            res_list.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join([str(item) for item in res_list])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # dfs builder: while N return
        # time: O(n) space: O(n)
        node_list = data.split(",")
        self.idx = 0
        n = len(node_list)
        def dfs():
            if node_list[self.idx]=="N":
                self.idx+=1
                return None
            val = int(node_list[self.idx])
            node = TreeNode(val)
            self.idx+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        




