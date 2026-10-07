class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        previous = [-(10**30)] * (len(nums2) + 1)
        for a in nums1:
            current = [-(10**30)]
            for j, b in enumerate(nums2, 1):
                current.append(
                    max(a * b + max(0, previous[j - 1]), previous[j], current[-1])
                )
            previous = current
        return previous[-1]
