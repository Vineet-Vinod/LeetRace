class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = [0] * n
        suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])
        prefix_max = nums[0]
        answer = 0
        for i in range(1, n - 1):
            if prefix_max < nums[i] < suffix[i + 1]:
                answer += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                answer += 1
            prefix_max = max(prefix_max, nums[i])
        return answer
