class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        frequency = [0] * (n + 1)
        for left, right in requests:
            frequency[left] += 1
            frequency[right + 1] -= 1
        for i in range(1, n):
            frequency[i] += frequency[i - 1]
        nums.sort()
        frequency = frequency[:n]
        frequency.sort()
        return sum(value * count for value, count in zip(nums, frequency)) % (10**9 + 7)
