class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = minimum = answer = nums[0]
        for value in nums[1:]:
            if value < 0:
                maximum, minimum = minimum, maximum
            maximum = max(value, maximum * value)
            minimum = min(value, minimum * value)
            answer = max(answer, maximum)
        return answer
