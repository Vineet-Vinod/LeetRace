class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        positions = [i for i, value in enumerate(nums) if value == 1]
        if not positions:
            return 0
        answer = 1
        for left, right in zip(positions, positions[1:]):
            answer = answer * (right - left) % (10**9 + 7)
        return answer
