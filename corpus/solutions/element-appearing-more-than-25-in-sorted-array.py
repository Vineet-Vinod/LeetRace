class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter

        return next(
            value for value, count in Counter(arr).items() if count * 4 > len(arr)
        )
