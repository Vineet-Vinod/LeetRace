class Solution:
    def rob(self, nums: List[int]) -> int:
        two_back = 0
        one_back = 0
        for amount in nums:
            two_back, one_back = one_back, max(one_back, two_back + amount)
        return one_back
