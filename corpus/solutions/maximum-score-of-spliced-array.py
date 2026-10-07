class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        best1 = best2 = running1 = running2 = 0
        for a, b in zip(nums1, nums2):
            running1 = max(0, running1 + b - a)
            running2 = max(0, running2 + a - b)
            best1 = max(best1, running1)
            best2 = max(best2, running2)
        return max(sum(nums1) + best1, sum(nums2) + best2)
