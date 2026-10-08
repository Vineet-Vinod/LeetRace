class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return sorted(nums, key=lambda value: (len(value), value), reverse=True)[k - 1]
