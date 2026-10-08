from collections import Counter


class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        half = len(s) // 2
        if max(Counter(s).values()) > half:
            return "-1"
        chars = sorted(s)
        left = "".join(chars[:half])
        right = "".join(chars[half:])
        pivot = left[-1]
        forbidden = len(left) - len(left.rstrip(pivot))
        count = right.count(pivot)
        if not count:
            return left + right
        higher = right[count:]
        return left + higher[:forbidden] + pivot * count + higher[forbidden:]
