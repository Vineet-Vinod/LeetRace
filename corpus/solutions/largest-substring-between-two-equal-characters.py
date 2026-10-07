class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first: dict[str, int] = {}
        best = -1
        for i, char in enumerate(s):
            if char in first:
                best = max(best, i - first[char] - 1)
            else:
                first[char] = i
        return best
