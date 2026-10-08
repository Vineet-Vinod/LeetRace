class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter

        return sum(count * (count - 1) // 2 for count in Counter(nums).values())
