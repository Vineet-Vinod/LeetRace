class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        paired = sum(count // 2 * 2 for count in counts.values())
        return paired + (paired < len(s))
