class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = sum(count // 2 for count in Counter(nums).values())
        return [pairs, len(nums) - 2 * pairs]
