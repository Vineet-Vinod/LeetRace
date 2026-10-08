from bisect import bisect_left


class Solution:
    def findMaximumLength(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        best = [0] * (n + 1)
        previous = [0] * (n + 2)
        for i in range(1, n + 1):
            previous[i] = max(previous[i], previous[i - 1])
            j = previous[i]
            best[i] = best[j] + 1
            target = 2 * prefix[i] - prefix[j]
            nxt = bisect_left(prefix, target, i + 1)
            previous[nxt] = i
        return best[n]
