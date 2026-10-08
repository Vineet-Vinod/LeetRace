class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = Counter()
        for row in matrix:
            key = tuple(value ^ row[0] for value in row)
            patterns[key] += 1
        return max(patterns.values())
