class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if 6 * len(nums1) < len(nums2) or 6 * len(nums2) < len(nums1):
            return -1
        difference = sum(nums1) - sum(nums2)
        if difference == 0:
            return 0
        if difference < 0:
            nums1, nums2 = nums2, nums1
            difference = -difference
        gains = [0] * 6
        for value in nums1:
            gains[value - 1] += 1
        for value in nums2:
            gains[6 - value] += 1
        operations = 0
        for gain in range(5, 0, -1):
            used = min(gains[gain], (difference + gain - 1) // gain)
            operations += used
            difference -= used * gain
            if difference <= 0:
                return operations
        return operations
