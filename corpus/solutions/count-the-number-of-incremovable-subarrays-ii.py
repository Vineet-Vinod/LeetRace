from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        while prefix + 1 < n and nums[prefix] < nums[prefix + 1]:
            prefix += 1
        if prefix == n - 1:
            return n * (n + 1) // 2
        answer = prefix + 2
        j = n - 1
        while j == n - 1 or nums[j] < nums[j + 1]:
            while prefix >= 0 and nums[prefix] >= nums[j]:
                prefix -= 1
            answer += prefix + 2
            j -= 1
        return answer
