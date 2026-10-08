class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        positions: dict[int, list[int]] = {}
        for index, value in enumerate(nums):
            positions.setdefault(value, []).append(index)
        answer = 0
        for indices in positions.values():
            left = 0
            for right, position in enumerate(indices):
                while position - indices[left] - (right - left) > k:
                    left += 1
                answer = max(answer, right - left + 1)
        return answer
