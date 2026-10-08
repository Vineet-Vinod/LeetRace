from bisect import bisect_left


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2

        def sums(values: List[int]) -> list[list[int]]:
            result = [[] for _ in range(n + 1)]
            result[0] = [0]
            for count, value in enumerate(values):
                for size in range(count + 1, 0, -1):
                    result[size].extend(total + value for total in result[size - 1])
            return result

        left, right = sums(nums[:n]), sums(nums[n:])
        total = sum(nums)
        answer = abs(total - 2 * sum(nums[:n]))
        for size, values in enumerate(left):
            other = sorted(right[n - size])
            for value in values:
                index = bisect_left(other, (total - 2 * value + 1) // 2)
                for j in (index - 1, index):
                    if 0 <= j < len(other):
                        answer = min(answer, abs(total - 2 * (value + other[j])))
        return answer
