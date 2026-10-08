class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0] * (len(nums2) + 1)
        best = 0
        for value in nums1:
            for j in range(len(nums2) - 1, -1, -1):
                if value == nums2[j]:
                    dp[j + 1] = dp[j] + 1
                    best = max(best, dp[j + 1])
                else:
                    dp[j + 1] = 0
        return best
