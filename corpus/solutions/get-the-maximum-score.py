from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        left = right = 0
        while i < len(nums1) or j < len(nums2):
            if j == len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]):
                left += nums1[i]
                i += 1
            elif i == len(nums1) or nums2[j] < nums1[i]:
                right += nums2[j]
                j += 1
            else:
                left = right = max(left, right) + nums1[i]
                i += 1
                j += 1
        return max(left, right) % (10**9 + 7)
