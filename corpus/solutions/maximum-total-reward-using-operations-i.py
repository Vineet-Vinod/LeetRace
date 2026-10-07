class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        reachable = 1
        for value in sorted(rewardValues):
            eligible = reachable & ((1 << value) - 1)
            reachable |= eligible << value
        return reachable.bit_length() - 1
