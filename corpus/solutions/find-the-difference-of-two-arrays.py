class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first, second = set(nums1), set(nums2)
        return [sorted(first - second), sorted(second - first)]
