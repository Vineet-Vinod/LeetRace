class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        if common:
            return min(common)
        first = min(nums1)
        second = min(nums2)
        return min(first * 10 + second, second * 10 + first)
