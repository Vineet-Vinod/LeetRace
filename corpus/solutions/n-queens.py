class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []

        def dfs(columns, rising, falling, board):
            row = len(board)
            if row == n:
                answer.append(board)
                return
            for col in range(n):
                if (
                    col not in columns
                    and row + col not in rising
                    and row - col not in falling
                ):
                    dfs(
                        columns | {col},
                        rising | {row + col},
                        falling | {row - col},
                        board + ["." * col + "Q" + "." * (n - col - 1)],
                    )

        dfs(set(), set(), set(), [])
        return sorted(answer)
