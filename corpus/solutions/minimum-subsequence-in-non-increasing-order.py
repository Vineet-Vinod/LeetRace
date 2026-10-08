class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums, reverse=True)
        selected = []
        left, right = sum(nums), 0
        for value in ordered:
            selected.append(value)
            right += value
            left -= value
            if right > left:
                break
        return selected
