from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        m = len(pattern)
        prefix = [0] * m
        length = 0
        for i in range(1, m):
            while length and pattern[i] != pattern[length]:
                length = prefix[length - 1]
            if pattern[i] == pattern[length]:
                length += 1
            prefix[i] = length
        answer = length = 0
        for a, b in zip(nums, nums[1:]):
            value = (b > a) - (b < a)
            while length and value != pattern[length]:
                length = prefix[length - 1]
            if value == pattern[length]:
                length += 1
            if length == m:
                answer += 1
                length = prefix[length - 1]
        return answer
