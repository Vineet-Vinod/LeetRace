class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first, second = set(nums1), set(nums2)
        common = first & second
        return min(common) if common else -1
