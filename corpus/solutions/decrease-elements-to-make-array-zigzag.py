class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        costs = [0, 0]
        for parity in (0, 1):
            for index, value in enumerate(nums):
                if index % 2 != parity:
                    continue
                neighbors = []
                if index > 0:
                    neighbors.append(nums[index - 1])
                if index + 1 < len(nums):
                    neighbors.append(nums[index + 1])
                if neighbors:
                    costs[parity] += max(0, value - min(neighbors) + 1)
        return min(costs)
