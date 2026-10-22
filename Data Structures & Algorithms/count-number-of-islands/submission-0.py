class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # out of boundary
            if i<0 or i>=m or j<0 or j>=n:
                return False
            # water
            if self.grid[i][j] == '0':
                return False
            # visited
            if self.visited[i][j] == 1:
                return False
            self.visited[i][j] = 1
            return dfs(i+1, j) or dfs(i, j+1) or dfs(i-1, j) or dfs(i, j-1)
        self.num_island = 0
        self.grid = grid
        m, n = len(grid), len(grid[0])
        self.visited = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == '1' and self.visited[i][j] == 0:
                    self.num_island += 1
                    dfs(i,j)
        return self.num_island