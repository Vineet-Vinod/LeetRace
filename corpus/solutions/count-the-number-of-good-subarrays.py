class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        counts: dict[int, int] = {}
        pairs = answer = left = 0
        for right, value in enumerate(nums):
            pairs += counts.get(value, 0)
            counts[value] = counts.get(value, 0) + 1
            while pairs >= k:
                answer += len(nums) - right
                old = nums[left]
                counts[old] -= 1
                pairs -= counts[old]
                left += 1
        return answer
