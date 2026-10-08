class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        pairs = len(nums) // 2
        reach = [0] * (k + 2)
        exact = [0] * (k + 1)
        for index in range(pairs):
            first = nums[index]
            second = nums[-index - 1]
            difference = abs(first - second)
            limit = max(first, second, k - first, k - second)
            reach[0] += 1
            reach[limit + 1] -= 1
            exact[difference] += 1

        one_change = 0
        answer = 2 * pairs
        for difference in range(k + 1):
            one_change += reach[difference]
            answer = min(answer, 2 * pairs - one_change - exact[difference])
        return answer
