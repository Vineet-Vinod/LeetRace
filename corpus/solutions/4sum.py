class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        values = sorted(nums)
        result = []
        size = len(values)
        for first in range(size - 3):
            if first and values[first] == values[first - 1]:
                continue
            for second in range(first + 1, size - 2):
                if second > first + 1 and values[second] == values[second - 1]:
                    continue
                left = second + 1
                right = size - 1
                while left < right:
                    total = (
                        values[first] + values[second] + values[left] + values[right]
                    )
                    if total == target:
                        result.append(
                            [values[first], values[second], values[left], values[right]]
                        )
                        left += 1
                        right -= 1
                        while left < right and values[left] == values[left - 1]:
                            left += 1
                        while left < right and values[right] == values[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result
