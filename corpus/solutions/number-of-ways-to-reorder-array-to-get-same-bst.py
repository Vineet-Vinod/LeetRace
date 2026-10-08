from math import comb


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        left = [-1] * len(nums)
        right = [-1] * len(nums)
        for i in range(1, len(nums)):
            node = 0
            while True:
                children = left if nums[i] < nums[node] else right
                if children[node] == -1:
                    children[node] = i
                    break
                node = children[node]
        sizes = [1] * len(nums)
        ways = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            a, b = left[i], right[i]
            na = sizes[a] if a != -1 else 0
            nb = sizes[b] if b != -1 else 0
            sizes[i] += na + nb
            ways[i] = (
                comb(na + nb, na)
                * (ways[a] if a != -1 else 1)
                * (ways[b] if b != -1 else 1)
                % 1_000_000_007
            )
        return (ways[0] - 1) % 1_000_000_007
