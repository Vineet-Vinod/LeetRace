class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways = {0: 1}
        for value in nums:
            next_ways: dict[int, int] = {}
            for subtotal, count in ways.items():
                next_ways[subtotal + value] = next_ways.get(subtotal + value, 0) + count
                next_ways[subtotal - value] = next_ways.get(subtotal - value, 0) + count
            ways = next_ways
        return ways.get(target, 0)
