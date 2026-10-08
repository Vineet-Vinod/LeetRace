class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        return [
            sum(value in set2 for value in nums1),
            sum(value in set1 for value in nums2),
        ]
