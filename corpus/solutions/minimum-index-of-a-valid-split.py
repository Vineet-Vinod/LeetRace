class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counts = Counter(nums)
        dominant = max(counts, key=counts.get)
        total = counts[dominant]
        prefix = 0
        for index, value in enumerate(nums[:-1]):
            prefix += value == dominant
            left_size = index + 1
            right_size = len(nums) - left_size
            if prefix * 2 > left_size and (total - prefix) * 2 > right_size:
                return index
        return -1
