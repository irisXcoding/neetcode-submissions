class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[0]*n for i in range(m)]
        def dfs(i, x, y):
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] == 1 or board[x][y] != word[i]:
                return False
            if i == len(word)-1:
                return True
            visited[x][y] = 1
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):

                if dfs(i+1, x+dx, y+dy):
                    return True
            visited[x][y] = 0
            return False


        for x in range(m):
            for y in range(n):
                if board[x][y]==word[0]:
                    if dfs(0, x, y):
                        return True
        return False