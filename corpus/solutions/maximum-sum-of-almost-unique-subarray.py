class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        counts: Dict[int, int] = defaultdict(int)
        total = 0
        answer = 0
        for index, value in enumerate(nums):
            counts[value] += 1
            total += value
            if index >= k:
                removed = nums[index - k]
                counts[removed] -= 1
                if counts[removed] == 0:
                    del counts[removed]
                total -= removed
            if index >= k - 1 and len(counts) >= m:
                answer = max(answer, total)
        return answer
