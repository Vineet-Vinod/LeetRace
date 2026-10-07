class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        first = second = best = 1
        for i in range(1, len(nums1)):
            next_first = next_second = 1
            if nums1[i] >= nums1[i - 1]:
                next_first = max(next_first, first + 1)
            if nums1[i] >= nums2[i - 1]:
                next_first = max(next_first, second + 1)
            if nums2[i] >= nums1[i - 1]:
                next_second = max(next_second, first + 1)
            if nums2[i] >= nums2[i - 1]:
                next_second = max(next_second, second + 1)
            first, second = next_first, next_second
            best = max(best, first, second)
        return best
