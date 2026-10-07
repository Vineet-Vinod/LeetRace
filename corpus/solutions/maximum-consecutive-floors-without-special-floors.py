class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        special.sort()
        longest = special[0] - bottom
        for previous, current in zip(special, special[1:]):
            longest = max(longest, current - previous - 1)
        return max(longest, top - special[-1])
