class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        from collections import defaultdict

        totals = defaultdict(int)
        for key, value in nums1 + nums2:
            totals[key] += value
        return [[key, totals[key]] for key in sorted(totals)]
