from functools import lru_cache


class Solution:
    def getMaxGridHappiness(
        self, m: int, n: int, introvertsCount: int, extrovertsCount: int
    ) -> int:
        m, n = max(m, n), min(m, n)
        return _happiness(m, n, 0, 0, introvertsCount, extrovertsCount)


@lru_cache(None)
def _happiness(m: int, n: int, pos: int, mask: int, intro: int, extro: int) -> int:
    if pos == m * n or not intro + extro:
        return 0
    power = 3 ** (n - 1)
    up = mask // power
    left = mask % 3 if pos % n else 0
    shifted = (mask % power) * 3
    best = _happiness(m, n, pos + 1, shifted, intro, extro)
    for person, remaining in [(1, intro), (2, extro)]:
        if not remaining:
            continue
        score = 120 if person == 1 else 40
        for neighbor in (up, left):
            if neighbor:
                score += (-30 if person == 1 else 20) + (-30 if neighbor == 1 else 20)
        score += _happiness(
            m,
            n,
            pos + 1,
            shifted + person,
            intro - (person == 1),
            extro - (person == 2),
        )
        best = max(best, score)
    return best
