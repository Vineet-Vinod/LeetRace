class Solution:
    def maxSubstringLength(self, s: str) -> int:
        first = {}
        last = {}
        for i, char in enumerate(s):
            first.setdefault(char, i)
            last[char] = i
        answer = -1
        for start in first.values():
            end = start
            for i in range(start, len(s)):
                char = s[i]
                if first[char] < start:
                    break
                end = max(end, last[char])
                if i >= end and i - start + 1 < len(s):
                    answer = max(answer, i - start + 1)
        return answer
