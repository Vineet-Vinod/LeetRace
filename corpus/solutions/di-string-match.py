class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        result = list(range(len(s) + 1))
        start = 0
        while start < len(s):
            if s[start] == "I":
                start += 1
                continue
            end = start
            while end < len(s) and s[end] == "D":
                end += 1
            result[start : end + 1] = reversed(result[start : end + 1])
            start = end
        return result
