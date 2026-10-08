class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        gaps = sorted(
            {
                nums[j] - nums[i]
                for i in range(n)
                for j in range(i + 1, n)
                if nums[j] > nums[i]
            }
        )
        mod = 10**9 + 7
        result = 0
        prev = 0
        for gap in gaps:
            end = []
            left = 0
            for i in range(n):
                while left < i and nums[i] - nums[left] >= gap:
                    left += 1
                end.append(left)
            dp = [1] * n
            for length in range(2, k + 1):
                prefix = [0]
                for count in dp:
                    prefix.append((prefix[-1] + count) % mod)
                dp = [prefix[e] for e in end]
            result = (result + (gap - prev) * sum(dp)) % mod
            prev = gap
        return result
