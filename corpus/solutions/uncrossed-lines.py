class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        previous = [0] * (len(nums2) + 1)
        for a in nums1:
            current = [0]
            for j, b in enumerate(nums2, 1):
                if a == b:
                    current.append(previous[j - 1] + 1)
                else:
                    current.append(max(previous[j], current[-1]))
            previous = current
        return previous[-1]
