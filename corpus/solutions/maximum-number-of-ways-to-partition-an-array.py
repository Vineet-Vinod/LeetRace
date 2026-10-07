from collections import Counter


class Solution:
    def waysToPartition(self, nums: list[int], k: int) -> int:
        total = sum(nums)
        prefix = 0
        diffs = []
        for x in nums[:-1]:
            prefix += x
            diffs.append(2 * prefix - total)
        right = Counter(diffs)
        left = Counter()
        answer = right[0]
        for i, x in enumerate(nums):
            delta = k - x
            answer = max(answer, left[delta] + right[-delta])
            if i < len(diffs):
                right[diffs[i]] -= 1
                left[diffs[i]] += 1
        return answer
