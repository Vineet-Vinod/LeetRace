class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for start in range(len(s)):
            counts = [0] * 26
            for end in range(start, len(s)):
                counts[ord(s[end]) - ord("a")] += 1
                nonzero = [count for count in counts if count]
                total += max(nonzero) - min(nonzero)
        return total
