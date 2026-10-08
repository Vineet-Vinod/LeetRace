class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        counts = Counter(
            value for value in arrays[0] if all(value in row for row in arrays[1:])
        )
        return sorted(counts)
