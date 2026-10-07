class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counts = Counter(nums[i + 1] for i in range(len(nums) - 1) if nums[i] == key)
        return min(counts, key=lambda x: (-counts[x], x))
