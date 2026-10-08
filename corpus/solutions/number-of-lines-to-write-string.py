class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        used = 0
        for ch in s:
            width = widths[ord(ch) - 97]
            if used + width > 100:
                lines += 1
                used = 0
            used += width
        return [lines, used]
