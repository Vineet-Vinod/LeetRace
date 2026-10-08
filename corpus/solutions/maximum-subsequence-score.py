from heapq import heappop, heappush


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ordered = sorted(zip(nums2, nums1), reverse=True)
        selected: list[int] = []
        total = 0
        best = 0
        for minimum, value in ordered:
            heappush(selected, value)
            total += value
            if len(selected) > k:
                total -= heappop(selected)
            if len(selected) == k:
                best = max(best, total * minimum)
        return best
