from collections import Counter


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        pivot = nums.index(k)
        counts = Counter({0: 1})
        balance = 0
        for i in range(pivot - 1, -1, -1):
            balance += 1 if nums[i] > k else -1
            counts[balance] += 1
        answer = counts[0] + counts[1]
        balance = 0
        for i in range(pivot + 1, len(nums)):
            balance += 1 if nums[i] > k else -1
            answer += counts[-balance] + counts[1 - balance]
        return answer
