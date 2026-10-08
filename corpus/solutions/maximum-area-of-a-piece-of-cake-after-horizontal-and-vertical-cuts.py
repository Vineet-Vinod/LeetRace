class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        def largest_gap(length: int, cuts: List[int]) -> int:
            ordered = [0] + sorted(cuts) + [length]
            return max(
                ordered[index + 1] - ordered[index] for index in range(len(ordered) - 1)
            )

        return (
            largest_gap(h, horizontalCuts) * largest_gap(w, verticalCuts) % (10**9 + 7)
        )
