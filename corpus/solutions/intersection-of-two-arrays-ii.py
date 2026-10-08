class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        result = []
        for value in nums2:
            if counts[value]:
                result.append(value)
                counts[value] -= 1
        return sorted(result)
