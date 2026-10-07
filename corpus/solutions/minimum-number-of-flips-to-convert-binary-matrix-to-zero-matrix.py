from collections import deque
from typing import List


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        state = sum(
            mat[r][c] << (r * cols + c) for r in range(rows) for c in range(cols)
        )
        moves = []
        for r in range(rows):
            for c in range(cols):
                mask = 0
                for rr, cc in ((r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= rr < rows and 0 <= cc < cols:
                        mask ^= 1 << (rr * cols + cc)
                moves.append(mask)
        queue = deque([(state, 0)])
        seen = {state}
        while queue:
            state, distance = queue.popleft()
            if state == 0:
                return distance
            for move in moves:
                nxt = state ^ move
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, distance + 1))
        return -1
