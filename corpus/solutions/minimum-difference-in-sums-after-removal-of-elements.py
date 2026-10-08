from heapq import heapify, heappushpop


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3
        heap = [-value for value in nums[:n]]
        heapify(heap)
        total = sum(nums[:n])
        left = [total]
        for value in nums[n : 2 * n]:
            total += value + heappushpop(heap, -value)
            left.append(total)
        heap = nums[2 * n :].copy()
        heapify(heap)
        total = sum(heap)
        answer = left[-1] - total
        for i in range(2 * n - 1, n - 1, -1):
            total += nums[i] - heappushpop(heap, nums[i])
            answer = min(answer, left[i - n] - total)
        return answer
