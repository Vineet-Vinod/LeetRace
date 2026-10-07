class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        total = 0
        moved = []
        operations = 0
        for value in nums:
            total += value
            if value < 0:
                heappush(moved, value)
            if total < 0:
                total -= heappop(moved)
                operations += 1
        return operations
