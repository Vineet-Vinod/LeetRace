class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def longest_run(bars: List[int]) -> int:
            ordered = sorted(bars)
            best = current = 0
            previous = None
            for bar in ordered:
                current = (
                    current + 1 if previous is not None and bar == previous + 1 else 1
                )
                best = max(best, current)
                previous = bar
            return best

        side = min(longest_run(hBars), longest_run(vBars)) + 1
        return side * side
