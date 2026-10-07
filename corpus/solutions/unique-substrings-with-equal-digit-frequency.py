class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        unique: set[str] = set()
        for start in range(len(s)):
            counts = [0] * 10
            distinct = 0
            maximum = 0
            for end in range(start, len(s)):
                digit = ord(s[end]) - ord("0")
                if counts[digit] == 0:
                    distinct += 1
                counts[digit] += 1
                maximum = max(maximum, counts[digit])
                if maximum * distinct == end - start + 1:
                    unique.add(s[start : end + 1])
        return len(unique)
