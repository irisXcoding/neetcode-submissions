# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        tree_list = []
        def dfs(node):
            if not node:
                tree_list.append("N")
                return
            tree_list.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(tree_list)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tree_list = data.split(",")
        self.index = 0
        def build():
            node_val = tree_list[self.index]
            self.index += 1 
            if node_val != "N":
                node = TreeNode(int(node_val))
                node.left = build()
                node.right = build()
            else:
                return None
            return node
        
        return build()
                






