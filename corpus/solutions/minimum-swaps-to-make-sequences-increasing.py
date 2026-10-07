class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        keep, swap = 0, 1
        for i in range(1, len(nums1)):
            next_keep = next_swap = 10**30
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                next_keep = keep
                next_swap = swap + 1
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                next_keep = min(next_keep, swap)
                next_swap = min(next_swap, keep + 1)
            keep, swap = next_keep, next_swap
        return min(keep, swap)
