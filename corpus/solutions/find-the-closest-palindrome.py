class Solution:
    def nearestPalindromic(self, n: str) -> str:
        size = len(n)
        prefix = int(n[: (size + 1) // 2])
        choices = {10 ** (size - 1) - 1, 10**size + 1}
        for p in (prefix - 1, prefix, prefix + 1):
            left = str(p)
            right = left[:-1] if size % 2 else left
            choices.add(int(left + right[::-1]))
        value = int(n)
        choices.discard(value)
        return str(min(choices, key=lambda x: (abs(x - value), x)))
