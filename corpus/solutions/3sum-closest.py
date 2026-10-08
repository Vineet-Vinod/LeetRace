class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        values = sorted(nums)
        best = values[0] + values[1] + values[2]
        for i in range(len(values) - 2):
            left = i + 1
            right = len(values) - 1
            while left < right:
                total = values[i] + values[left] + values[right]
                if abs(total - target) < abs(best - target) or (
                    abs(total - target) == abs(best - target) and total < best
                ):
                    best = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return best
