from functools import lru_cache


class Solution:
    def closestFair(self, n: int) -> int:
        lower = str(n)
        for length in range(len(lower), len(lower) + 3):
            if length % 2:
                continue
            bound = lower if length == len(lower) else "0" * length
            half = length // 2

            @lru_cache(maxsize=None)
            def build(position: int, odds: int, evens: int, tight: bool) -> str | None:
                if position == length:
                    return "" if odds == evens == half else None
                minimum = int(bound[position]) if tight else 0
                if position == 0:
                    minimum = max(minimum, 1)
                for digit in range(minimum, 10):
                    is_odd = digit % 2
                    next_odds = odds + is_odd
                    next_evens = evens + (1 - is_odd)
                    if next_odds > half or next_evens > half:
                        continue
                    suffix = build(
                        position + 1,
                        next_odds,
                        next_evens,
                        tight and digit == int(bound[position]),
                    )
                    if suffix is not None:
                        return str(digit) + suffix
                return None

            answer = build(0, 0, 0, length == len(lower))
            if answer is not None:
                return int(answer)
        raise ValueError("No fair integer found within the searched digit lengths")
