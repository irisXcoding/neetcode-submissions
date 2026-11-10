class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i > m - 1 or j > n - 1 or visited[i][j] == 1 or grid[i][j] == "0":
                return
            visited[i][j] = 1
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(i + dx, j + dy)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    dfs(i, j)
        return count