class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for value in arr:
            if value <= k:
                k += 1
            else:
                break
        return k
