from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        while low <= high:
            a = (low + high) // 2
            b = (m + n + 1) // 2 - a
            al = nums1[a - 1] if a else -float("inf")
            ar = nums1[a] if a < m else float("inf")
            bl = nums2[b - 1] if b else -float("inf")
            br = nums2[b] if b < n else float("inf")
            if al > br:
                high = a - 1
            elif bl > ar:
                low = a + 1
            else:
                return (
                    float(max(al, bl))
                    if (m + n) % 2
                    else (max(al, bl) + min(ar, br)) / 2
                )
        raise ValueError("Unsorted arrays")
