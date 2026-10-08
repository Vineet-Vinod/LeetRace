class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        groups = 0
        smallest = None
        for value in nums:
            if smallest is None or value - smallest > k:
                groups += 1
                smallest = value
        return groups
