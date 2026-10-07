class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        repeated_pairs = 0
        best = 1
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                repeated_pairs += 1
            while repeated_pairs > 1:
                if s[left] == s[left + 1]:
                    repeated_pairs -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
