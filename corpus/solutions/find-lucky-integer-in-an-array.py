class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter

        counts = Counter(arr)
        return max(
            (value for value, count in counts.items() if value == count), default=-1
        )
