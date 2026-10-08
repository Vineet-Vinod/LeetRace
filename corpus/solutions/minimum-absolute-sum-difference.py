class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        modulo = 10**9 + 7
        ordered = sorted(nums1)
        total = 0
        best_reduction = 0
        for first, second in zip(nums1, nums2):
            difference = abs(first - second)
            total += difference
            index = bisect_left(ordered, second)
            if index < len(ordered):
                best_reduction = max(
                    best_reduction, difference - abs(ordered[index] - second)
                )
            if index > 0:
                best_reduction = max(
                    best_reduction, difference - abs(ordered[index - 1] - second)
                )
        return (total - best_reduction) % modulo
