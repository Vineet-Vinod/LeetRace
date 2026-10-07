class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        if k == 0:
            return sum(count >= 2 for count in counts.values())
        return sum(value + k in counts for value in counts)
