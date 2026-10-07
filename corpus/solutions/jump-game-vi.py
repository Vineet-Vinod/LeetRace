class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        best = [0] * len(nums)
        best[0] = nums[0]
        candidates = deque([0])
        for i in range(1, len(nums)):
            while candidates[0] < i - k:
                candidates.popleft()
            best[i] = best[candidates[0]] + nums[i]
            while candidates and best[candidates[-1]] <= best[i]:
                candidates.pop()
            candidates.append(i)
        return best[-1]
