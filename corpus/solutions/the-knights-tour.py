class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        board = [[-1] * n for _ in range(m)]
        board[r][c] = 0
        path = [(r, c)]

        def search(x: int, y: int) -> bool:
            if len(path) == m * n:
                return True
            options = []
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == -1:
                    degree = sum(
                        0 <= nx + ax < m
                        and 0 <= ny + ay < n
                        and board[nx + ax][ny + ay] == -1
                        for ax, ay in moves
                    )
                    options.append((degree, nx, ny))
            for _, nx, ny in sorted(options):
                board[nx][ny] = len(path)
                path.append((nx, ny))
                if search(nx, ny):
                    return True
                path.pop()
                board[nx][ny] = -1
            return False

        search(r, c)
        return board
