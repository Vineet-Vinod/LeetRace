from collections import deque
from functools import cache


@cache
def distances():
    start = (1, 2, 3, 4, 5, 0)
    result = {start: 0}
    queue = deque([start])
    neighbors = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
    while queue:
        state = queue.popleft()
        z = state.index(0)
        for j in neighbors[z]:
            a = list(state)
            a[z], a[j] = a[j], a[z]
            nxt = tuple(a)
            if nxt not in result:
                result[nxt] = result[state] + 1
                queue.append(nxt)
    return result


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        return distances().get(tuple(board[0] + board[1]), -1)
