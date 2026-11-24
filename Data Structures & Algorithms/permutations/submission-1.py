class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False]*n
        self.path = []
        res = []
        def dfs():
            if len(self.path) == n:
                res.append(self.path[:])
                path = []
                return
            for i in range(n):
                if not visited[i]:
                    self.path.append(nums[i])
                    visited[i] = True
                    dfs()
                    self.path.pop(-1)
                    visited[i] = False
        dfs()
        return res
        