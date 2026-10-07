class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        score = [[-1] * (n + 1) for _ in range(n + 1)]
        ways = [[0] * (n + 1) for _ in range(n + 1)]
        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1
        for row in range(n - 1, -1, -1):
            for column in range(n - 1, -1, -1):
                if board[row][column] in "XS":
                    continue
                neighbors = [
                    (row + 1, column),
                    (row, column + 1),
                    (row + 1, column + 1),
                ]
                best = max(score[a][b] for a, b in neighbors)
                if best < 0:
                    continue
                score[row][column] = best + (
                    int(board[row][column]) if board[row][column] != "E" else 0
                )
                ways[row][column] = sum(
                    ways[a][b] for a, b in neighbors if score[a][b] == best
                ) % (10**9 + 7)
        return [score[0][0], ways[0][0]] if score[0][0] >= 0 else [0, 0]
