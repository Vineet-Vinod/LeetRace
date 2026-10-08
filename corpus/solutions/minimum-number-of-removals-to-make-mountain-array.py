from bisect import bisect_left


class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        def lis(values: list[int]) -> list[int]:
            tails = []
            lengths = []
            for x in values:
                i = bisect_left(tails, x)
                if i == len(tails):
                    tails.append(x)
                else:
                    tails[i] = x
                lengths.append(i + 1)
            return lengths

        left = lis(nums)
        right = lis(nums[::-1])[::-1]
        best = max(a + b - 1 for a, b in zip(left, right) if a > 1 and b > 1)
        return len(nums) - best
