class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        best = [0] * (len(s) + 1)
        for end in range(1, len(s) + 1):
            best[end] = best[end - 1] + 1
            for start in range(end):
                if s[start:end] in words:
                    best[end] = min(best[end], best[start])
        return best[-1]
