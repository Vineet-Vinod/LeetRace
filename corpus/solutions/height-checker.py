class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(
            actual != expected for actual, expected in zip(heights, sorted(heights))
        )
