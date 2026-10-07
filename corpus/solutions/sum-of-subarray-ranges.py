class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            lo = hi = nums[i]
            for j in range(i, n):
                lo = min(lo, nums[j])
                hi = max(hi, nums[j])
                answer += hi - lo
        return answer
