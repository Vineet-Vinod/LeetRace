class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        low, high = min(nums), max(nums)
        if low == high:
            return 0
        size = max(1, (high - low + len(nums) - 2) // (len(nums) - 1))
        bucket_count = (high - low) // size + 1
        minima = [inf] * bucket_count
        maxima = [-inf] * bucket_count
        for value in nums:
            index = (value - low) // size
            minima[index] = min(minima[index], value)
            maxima[index] = max(maxima[index], value)
        answer = 0
        previous = low
        for index in range(bucket_count):
            if minima[index] == inf:
                continue
            answer = max(answer, int(minima[index] - previous))
            previous = int(maxima[index])
        return answer
