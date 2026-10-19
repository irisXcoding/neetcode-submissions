# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res_list = []
        def dfs(node):
            if not node:
                res_list.append("N")
                return
            res_list.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(",".join(res_list))
        return ",".join(res_list)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_list = data.split(",")
        if not data:
            return None
        self.cur_idx = 0
        def rebuild():
            if self.cur_idx>len(data_list)-1:
                return None
            val = data_list[self.cur_idx]
            self.cur_idx+=1
            if val == "N":
                return None
            val_int = int(val)
            node = TreeNode(val_int)
            node.left = rebuild()
            node.right = rebuild()
            return node
        return rebuild()





