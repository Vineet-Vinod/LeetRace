from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = -1
        for digits in permutations(arr):
            hours = digits[0] * 10 + digits[1]
            minutes = digits[2] * 10 + digits[3]
            if hours < 24 and minutes < 60:
                best = max(best, hours * 60 + minutes)
        if best < 0:
            return ""
        return f"{best // 60:02d}:{best % 60:02d}"
