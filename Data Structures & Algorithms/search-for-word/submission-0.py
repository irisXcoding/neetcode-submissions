class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtrack(idx, x, y), idx=idx of letter in word, x&y=position of board
        # go 4 direction to check: 1. out of boundary 2. if visited 3. if the letter same
        # complexity: time: O(m*n4^L) space:O(m*n)
        def backtrack(i, x, y):
            if i>=len(word) or x >= m or x < 0 or y >= n or y < 0 or visited[x][y] == 1 or board[x][y] != word[i]:
                return False
            if board[x][y] == word[i] and i == len(word) - 1:
                return True
            # print(i, word[i])
            # print(x,y, board[x][y])
            # print(visited)
            # update visited
            visited[x][y] = 1
            # go 4 direction
            for dx, dy in [(1,0), (0,1), (-1, 0), (0, -1)]:
                if backtrack(i+1, x+dx, y+dy):
                    visited[x][y] = 0
                    return True
            visited[x][y] = 0
            return False
            

        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(0, i, j):
                        return True
        return False
