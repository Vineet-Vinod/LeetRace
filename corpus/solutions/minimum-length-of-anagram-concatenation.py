class Solution:
    def minAnagramLength(self, s: str) -> int:
        size = len(s)
        for length in range(1, size + 1):
            if size % length:
                continue
            expected = Counter(s[:length])
            if all(
                Counter(s[start : start + length]) == expected
                for start in range(length, size, length)
            ):
                return length
        return size
