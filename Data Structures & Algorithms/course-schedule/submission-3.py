from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            # done -> True
            if status_dict[node] == 2:
                return True
            # in process -> False
            if status_dict[node] == 1:
                return False
            # mark
            status_dict[node] = 1
            # go through children
            courses = pre_map.get(node, [])
            for course in courses:
                if not dfs(course):
                    return False

            status_dict[node] = 2
            return True

        # edge case
        if not prerequisites:
            return True
        # get the graph dict
        pre_map = defaultdict(list)
        for before, after in prerequisites:
            pre_map[after].append(before)
        # status dict
        status_dict = {}
        for i in range(numCourses):
            status_dict[i] = 0
        # go through the pairs
        for pre in pre_map.keys():
            if not dfs(pre):
                return False

        return True

