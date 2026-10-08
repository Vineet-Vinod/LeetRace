class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum(a % (b * k) == 0 for a in nums1 for b in nums2)
