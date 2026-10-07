class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        if any(
            board[i][j] ^ board[i][0] ^ board[0][j] ^ board[0][0]
            for i in range(n)
            for j in range(n)
        ):
            return -1

        def swaps(bits):
            if not n // 2 <= sum(bits) <= (n + 1) // 2:
                return -1
            costs = []
            for start in (0, 1):
                target = [(i + start) % 2 for i in range(n)]
                if sum(target) == sum(bits):
                    costs.append(sum(a != b for a, b in zip(bits, target)) // 2)
            return min(costs)

        a = swaps(board[0])
        b = swaps([row[0] for row in board])
        return -1 if a < 0 or b < 0 else a + b
