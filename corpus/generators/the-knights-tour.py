DOMAIN_SIZE = 0


def generate(seed: int = 0) -> list[str]:
    # The entire input domain has at most 225 (m, n, r, c) tuples: sum(m*n, m,n=1..5).
    # Enumerate every tuple and retain exactly those promised by the statement (a tour exists).
    moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
    calls = []
    for m in range(1, 6):
        for n in range(1, 6):
            for r in range(m):
                for c in range(n):
                    board = [[False] * n for _ in range(m)]
                    board[r][c] = True
                    path = [(r, c)]

                    def search(x: int, y: int) -> bool:
                        if len(path) == m * n:
                            return True
                        options = []
                        for dx, dy in moves:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and not board[nx][ny]:
                                degree = sum(
                                    0 <= nx + ax < m
                                    and 0 <= ny + ay < n
                                    and not board[nx + ax][ny + ay]
                                    for ax, ay in moves
                                )
                                options.append((degree, nx, ny))
                        for _, nx, ny in sorted(options):
                            board[nx][ny] = True
                            path.append((nx, ny))
                            if search(nx, ny):
                                return True
                            path.pop()
                            board[nx][ny] = False
                        return False

                    if search(r, c):
                        calls.append(f"candidate(m={m}, n={n}, r={r}, c={c})")
    global DOMAIN_SIZE
    DOMAIN_SIZE = len(calls)
    return calls
