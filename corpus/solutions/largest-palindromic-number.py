class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = [0] * 10
        for digit in num:
            counts[ord(digit) - 48] += 1
        left = []
        for digit in range(9, -1, -1):
            left.append(str(digit) * (counts[digit] // 2))
        left = "".join(left).lstrip("0")
        center = next(
            (str(digit) for digit in range(9, -1, -1) if counts[digit] % 2), ""
        )
        if not left:
            return center or "0"
        return left + center + left[::-1]
