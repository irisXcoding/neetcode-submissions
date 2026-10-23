from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        status_dict = {}  # 1: in progess 2: done
        def dfs(node):
            status = status_dict.get(node, 0)
            if status == 1:
                return False
            if status == 2:
                return True
            else:
                status_dict[node] = 1
            nxt_nodes = graph.get(node, [])
            for nxt_node in nxt_nodes:
                if not dfs(nxt_node):
                    return False
            order.append(node)
            status_dict[node] = 2
            return True

        # build graph
        graph = defaultdict(list)
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        
        # go through all the node
        for i in range(numCourses):
            if not dfs(i):
                return []
        # 
        return list(reversed(order))
        