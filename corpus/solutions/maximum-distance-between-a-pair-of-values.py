class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        first = second = best = 0
        while first < len(nums1) and second < len(nums2):
            if first <= second and nums1[first] <= nums2[second]:
                best = max(best, second - first)
                second += 1
            else:
                first += 1
                if second < first:
                    second = first
        return best
