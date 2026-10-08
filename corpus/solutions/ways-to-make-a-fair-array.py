class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        right_even = sum(nums[::2])
        right_odd = sum(nums[1::2])
        left_even = left_odd = answer = 0
        for i, value in enumerate(nums):
            if i % 2 == 0:
                right_even -= value
            else:
                right_odd -= value
            answer += left_even + right_odd == left_odd + right_even
            if i % 2 == 0:
                left_even += value
            else:
                left_odd += value
        return answer
