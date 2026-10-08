class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        good = 0
        for index, value in enumerate(nums):
            key = value - index
            good += seen[key]
            seen[key] += 1
        total = len(nums) * (len(nums) - 1) // 2
        return total - good
