class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        modulo = 10**9 + 7
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        total = prefix[-1]
        answer = 0
        middle_start = 2
        middle_end = 2
        for left_end in range(1, len(nums) - 1):
            middle_start = max(middle_start, left_end + 1)
            while (
                middle_start < len(nums)
                and prefix[middle_start] - prefix[left_end] < prefix[left_end]
            ):
                middle_start += 1
            middle_end = max(middle_end, middle_start)
            while (
                middle_end < len(nums)
                and total - prefix[middle_end] >= prefix[middle_end] - prefix[left_end]
            ):
                middle_end += 1
            answer += max(0, middle_end - middle_start)
        return answer % modulo
