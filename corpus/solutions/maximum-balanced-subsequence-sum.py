from bisect import bisect_left


class Solution:
    def maxBalancedSubsequenceSum(self, nums: list[int]) -> int:
        keys = sorted(set(x - i for i, x in enumerate(nums)))
        bit = [0] * (len(keys) + 1)
        answer = max(nums)
        for i, x in enumerate(nums):
            pos = bisect_left(keys, x - i) + 1
            j = pos
            best = 0
            while j:
                best = max(best, bit[j])
                j -= j & -j
            value = best + x
            answer = max(answer, value)
            while pos < len(bit):
                bit[pos] = max(bit[pos], value)
                pos += pos & -pos
        return answer
