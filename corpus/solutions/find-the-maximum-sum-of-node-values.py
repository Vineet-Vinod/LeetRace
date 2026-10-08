class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        even, odd = 0, float("-inf")
        for value in nums:
            changed = value ^ k
            even, odd = (
                max(even + value, odd + changed),
                max(odd + value, even + changed),
            )
        return int(even)
