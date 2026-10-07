class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        ordered = sorted(nums)
        mid = len(nums) // 2
        answer = abs(ordered[mid] - k)
        for x in ordered[:mid]:
            if x > k:
                answer += x - k
        for x in ordered[mid + 1 :]:
            if x < k:
                answer += k - x
        return answer
