class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i<0 or i>=self.m or j<0 or j>=self.n:
                return False
            if self.visited[i][j] == 1:
                return False
            if grid[i][j] == "0":
                return False
            self.visited[i][j] = 1
            
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
            
        self.m, self.n = len(grid), len(grid[0])
        self.visited = [[0 for j in range(self.n)] for i in range(self.m)]
        num_island = 0
        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i][j] and grid[i][j] == "1":
                    num_island+=1
                    dfs(i, j)
        return num_island