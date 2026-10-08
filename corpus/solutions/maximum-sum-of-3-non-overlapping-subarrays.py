class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        sums = []
        total = sum(nums[:k])
        sums.append(total)
        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]
            sums.append(total)
        m = len(sums)
        left = [0] * m
        for i in range(1, m):
            left[i] = i if sums[i] > sums[left[i - 1]] else left[i - 1]
        right = [m - 1] * m
        for i in range(m - 2, -1, -1):
            right[i] = i if sums[i] >= sums[right[i + 1]] else right[i + 1]
        answer = []
        best = -1
        for b in range(k, m - k):
            a, c = left[b - k], right[b + k]
            score = sums[a] + sums[b] + sums[c]
            if score > best:
                best = score
                answer = [a, b, c]
        return answer
