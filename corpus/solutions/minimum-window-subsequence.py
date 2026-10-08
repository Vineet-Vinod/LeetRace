class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        starts = [-1] * len(s2)
        best_start, best_length = 0, len(s1) + 1
        for i, char in enumerate(s1):
            for j in range(len(s2) - 1, -1, -1):
                if char == s2[j]:
                    starts[j] = i if j == 0 else starts[j - 1]
            if char == s2[-1] and starts[-1] >= 0:
                length = i - starts[-1] + 1
                if length < best_length:
                    best_start, best_length = starts[-1], length
        return (
            "" if best_length > len(s1) else s1[best_start : best_start + best_length]
        )
