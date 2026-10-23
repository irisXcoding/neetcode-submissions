from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        status = {}  # 1: in progress 2: done
        def dfs(node):
            if status.get(node, 0)==1:
                return False
            if status.get(node, 0)==2:
                return True
            else:
                status[node] = 1
            nxt = nxt_map.get(node, [])
            for nxt_node in nxt:
                if not dfs(nxt_node):
                    return False
            status[node] = 2
            return True
        # empty
        if not prerequisites:
            return True
        # log the pe-nxt pair
        nxt_map = defaultdict(list)
        for pair in prerequisites:
            nxt_map[pair[1]].append(pair[0])
        
        # dfs to detect cycle
        for pre in nxt_map.keys():
            if not dfs(pre):
                return False
        return True
