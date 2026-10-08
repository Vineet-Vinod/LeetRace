class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        counts = Counter(set(nums1)) + Counter(set(nums2)) + Counter(set(nums3))
        return sorted(value for value, count in counts.items() if count >= 2)
