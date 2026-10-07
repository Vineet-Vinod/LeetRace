class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: list[int] = []
        for value in nums:
            position = bisect_left(tails, value)
            if position == len(tails):
                tails.append(value)
            else:
                tails[position] = value
        return len(tails)
