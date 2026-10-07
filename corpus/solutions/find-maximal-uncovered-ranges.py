class Solution:
    def findMaximalUncoveredRanges(
        self, n: int, ranges: List[List[int]]
    ) -> List[List[int]]:
        covered = sorted(ranges)
        gaps: List[List[int]] = []
        next_uncovered = 0
        for left, right in covered:
            if left > next_uncovered:
                gaps.append([next_uncovered, left - 1])
            next_uncovered = max(next_uncovered, right + 1)
            if next_uncovered >= n:
                break
        if next_uncovered < n:
            gaps.append([next_uncovered, n - 1])
        return gaps
