class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        size = len(nums)
        left_min = [0] * size
        right_min = [0] * size
        left_min[0] = nums[0]
        for index in range(1, size):
            left_min[index] = min(left_min[index - 1], nums[index])
        right_min[-1] = nums[-1]
        for index in range(size - 2, -1, -1):
            right_min[index] = min(right_min[index + 1], nums[index])
        answer = float("inf")
        for peak in range(1, size - 1):
            if left_min[peak - 1] < nums[peak] and right_min[peak + 1] < nums[peak]:
                answer = min(
                    answer, left_min[peak - 1] + nums[peak] + right_min[peak + 1]
                )
        return -1 if answer == float("inf") else int(answer)
