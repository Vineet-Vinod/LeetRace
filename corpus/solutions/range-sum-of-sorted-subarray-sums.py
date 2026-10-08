class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for start in range(n):
            total = 0
            for end in range(start, n):
                total += nums[end]
                sums.append(total)
        sums.sort()
        return sum(sums[left - 1 : right]) % (10**9 + 7)
