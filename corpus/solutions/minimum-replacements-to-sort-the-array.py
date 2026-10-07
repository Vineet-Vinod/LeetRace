class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        bound = nums[-1]
        answer = 0
        for x in reversed(nums[:-1]):
            parts = (x + bound - 1) // bound
            answer += parts - 1
            bound = x // parts
        return answer
