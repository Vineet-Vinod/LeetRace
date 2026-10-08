class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive = 0
        negative = 0
        longest = 0
        for value in nums:
            if value == 0:
                positive = 0
                negative = 0
            elif value > 0:
                positive += 1
                negative = negative + 1 if negative else 0
            else:
                positive, negative = negative + 1 if negative else 0, positive + 1
            longest = max(longest, positive)
        return longest
