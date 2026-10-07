class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counts = Counter(text)
        best = 0
        for char in counts:
            left = 0
            other_chars = 0
            for right, value in enumerate(text):
                if value != char:
                    other_chars += 1
                while other_chars > 1:
                    if text[left] != char:
                        other_chars -= 1
                    left += 1
                best = max(best, min(right - left + 1, counts[char]))
        return best
