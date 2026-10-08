class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start = best_length = 0
        for center in range(len(s)):
            for left, right in ((center, center), (center, center + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    length = right - left + 1
                    if length > best_length:
                        best_start, best_length = left, length
                    left -= 1
                    right += 1
        return s[best_start : best_start + best_length]
