from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        for value in sorted(counts, key=abs):
            if counts[value] > counts[2 * value]:
                return False
            counts[2 * value] -= counts[value]
        return True
