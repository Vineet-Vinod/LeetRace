from typing import List
from functools import lru_cache


class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        return list(_rounds(n, firstPlayer, secondPlayer))


@lru_cache(None)
def _rounds(n: int, a: int, b: int) -> tuple[int, int]:
    if a + b == n + 1:
        return 1, 1
    states = {(0, 0)}
    for left in range(1, (n + 1) // 2 + 1):
        right = n + 1 - left
        if left > right:
            break
        if a in (left, right):
            choices = [a]
        elif b in (left, right):
            choices = [b]
        elif left == right:
            choices = [left]
        else:
            choices = [left, right]
        states = {
            (x + (winner < a), y + (winner < b))
            for x, y in states
            for winner in choices
        }
    earliest = n
    latest = 0
    for x, y in states:
        lo, hi = _rounds((n + 1) // 2, x + 1, y + 1)
        earliest = min(earliest, lo + 1)
        latest = max(latest, hi + 1)
    return earliest, latest
