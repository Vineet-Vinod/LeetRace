class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        if len(nums2) % 2:
            for value in nums1:
                result ^= value
        if len(nums1) % 2:
            for value in nums2:
                result ^= value
        return result
