class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nonincreasing_ending = [1] * n
        nondecreasing_starting = [1] * n
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                nonincreasing_ending[i] = nonincreasing_ending[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                nondecreasing_starting[i] = nondecreasing_starting[i + 1] + 1
        return [
            i
            for i in range(k, n - k)
            if nonincreasing_ending[i - 1] >= k and nondecreasing_starting[i + 1] >= k
        ]
