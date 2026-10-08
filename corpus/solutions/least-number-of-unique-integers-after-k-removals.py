class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = sorted(Counter(arr).values())
        remaining = len(counts)
        for count in counts:
            if k < count:
                break
            k -= count
            remaining -= 1
        return remaining
