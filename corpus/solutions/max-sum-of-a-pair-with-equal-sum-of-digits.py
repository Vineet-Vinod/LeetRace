class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        largest_by_digit_sum = {}
        answer = -1
        for value in nums:
            digit_sum = sum(int(char) for char in str(value))
            previous = largest_by_digit_sum.get(digit_sum)
            if previous is not None:
                answer = max(answer, previous + value)
            largest_by_digit_sum[digit_sum] = max(previous or 0, value)
        return answer
