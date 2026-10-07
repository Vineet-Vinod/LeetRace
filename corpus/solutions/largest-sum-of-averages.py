class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        best = [float("-inf")] * (len(nums) + 1)
        best[0] = 0.0
        answer = 0.0
        for groups in range(1, k + 1):
            current = [float("-inf")] * (len(nums) + 1)
            for end in range(1, len(nums) + 1):
                for start in range(end):
                    if best[start] != float("-inf"):
                        average = (prefix[end] - prefix[start]) / (end - start)
                        current[end] = max(current[end], best[start] + average)
            best = current
            answer = max(answer, best[-1])
        return answer
