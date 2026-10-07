class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        balance = 0
        longest = 0
        for index, value in enumerate(nums):
            balance += 1 if value == 1 else -1
            if balance in first_seen:
                longest = max(longest, index - first_seen[balance])
            else:
                first_seen[balance] = index
        return longest
