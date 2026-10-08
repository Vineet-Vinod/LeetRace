class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for row in range(8):
            for col in range(8):
                if board[row][col] == "R":
                    captures = 0
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        r, c = row + dr, col + dc
                        while 0 <= r < 8 and 0 <= c < 8:
                            if board[r][c] == "p":
                                captures += 1
                                break
                            if board[r][c] != ".":
                                break
                            r += dr
                            c += dc
                    return captures
        return 0
