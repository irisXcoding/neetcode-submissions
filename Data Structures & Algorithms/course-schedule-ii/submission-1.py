from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.course_list = []
        def dfs(node):
            # done -> True
            if status_dict.get(node,0) == 2:
                return True
            # in process -> False
            if status_dict.get(node,0) == 1:
                return False
            # mark
            status_dict[node] = 1
            # go through children
            courses = pre_map.get(node, [])
            for course in courses:
                if not dfs(course):
                    return False
            status_dict[node] = 2
            if node not in self.course_list:
                self.course_list.append(node)
            return True

        # get the graph dict
        pre_map = defaultdict(list)
        for before, after in prerequisites:
            pre_map[after].append(before)
        # status dict
        status_dict = {}
        for i in range(numCourses):
            status_dict[i] = 0
            if not dfs(i):
                return []

        return self.course_list[::-1]
        