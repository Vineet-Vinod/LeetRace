class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        odd_count = 0
        answer = 0
        for value in nums:
            odd_count += value % 2
            answer += counts.get(odd_count - k, 0)
            counts[odd_count] = counts.get(odd_count, 0) + 1
        return answer
