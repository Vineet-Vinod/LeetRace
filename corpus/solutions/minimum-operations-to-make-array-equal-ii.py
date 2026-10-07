class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        positive = negative = 0
        for a, b in zip(nums1, nums2):
            difference = a - b
            if difference % k:
                return -1
            units = difference // k
            if units > 0:
                positive += units
            else:
                negative -= units
        return positive if positive == negative else -1
