class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        score = 0
        earliest: dict[int, int] = {}
        best = 0
        for i, hour in enumerate(hours):
            score += 1 if hour > 8 else -1
            if score > 0:
                best = i + 1
            else:
                earliest.setdefault(score, i)
                if score - 1 in earliest:
                    best = max(best, i - earliest[score - 1])
        return best
