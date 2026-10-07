class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        minimum1 = sum1 + nums1.count(0)
        minimum2 = sum2 + nums2.count(0)
        if minimum1 == minimum2:
            return minimum1
        if minimum1 < minimum2 and nums1.count(0) == 0:
            return -1
        if minimum2 < minimum1 and nums2.count(0) == 0:
            return -1
        return max(minimum1, minimum2)
