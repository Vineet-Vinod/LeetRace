class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        positions = [index for index, value in enumerate(nums) if value]
        adjusted = [position - index for index, position in enumerate(positions)]
        prefix = [0]
        for value in adjusted:
            prefix.append(prefix[-1] + value)
        answer = 10**30
        for left in range(len(adjusted) - k + 1):
            right = left + k
            middle = left + k // 2
            median = adjusted[middle]
            cost = median * (middle - left) - (prefix[middle] - prefix[left])
            cost += prefix[right] - prefix[middle + 1] - median * (right - middle - 1)
            answer = min(answer, cost)
        return answer
