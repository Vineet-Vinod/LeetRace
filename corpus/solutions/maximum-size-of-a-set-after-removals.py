class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        limit = len(nums1) // 2
        first, second = set(nums1), set(nums2)
        only_first = len(first - second)
        only_second = len(second - first)
        common = len(first & second)
        take_first = min(limit, only_first)
        take_second = min(limit, only_second)
        remaining_slots = len(nums1) - take_first - take_second
        return take_first + take_second + min(common, remaining_slots)
