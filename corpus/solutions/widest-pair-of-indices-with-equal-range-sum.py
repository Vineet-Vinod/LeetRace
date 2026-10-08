class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        earliest = {0: -1}
        difference = 0
        best = 0
        for index, (first, second) in enumerate(zip(nums1, nums2)):
            difference += first - second
            if difference in earliest:
                best = max(best, index - earliest[difference])
            else:
                earliest[difference] = index
        return best
