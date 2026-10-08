from __future__ import annotations


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        values = [ord(c) - 97 for c in word]
        answer = 0
        start = 0
        for end in range(1, len(values) + 1):
            if end < len(values) and abs(values[end] - values[end - 1]) <= 2:
                continue
            for distinct in range(1, 27):
                length = distinct * k
                if length > end - start:
                    break
                counts = [0] * 26
                exact = 0
                for right in range(start, end):
                    c = values[right]
                    exact -= counts[c] == k
                    counts[c] += 1
                    exact += counts[c] == k
                    if right - start >= length:
                        c = values[right - length]
                        exact -= counts[c] == k
                        counts[c] -= 1
                        exact += counts[c] == k
                    if right - start + 1 >= length and exact == distinct:
                        answer += 1
            start = end
        return answer
