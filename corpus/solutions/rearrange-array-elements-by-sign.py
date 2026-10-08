class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [value for value in nums if value > 0]
        negative = [value for value in nums if value < 0]
        result = []
        for a, b in zip(positive, negative):
            result.extend((a, b))
        return result
