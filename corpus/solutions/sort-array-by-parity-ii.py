class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        evens = iter(sorted(value for value in nums if value % 2 == 0))
        odds = iter(sorted(value for value in nums if value % 2 == 1))
        return [
            next(evens) if index % 2 == 0 else next(odds) for index in range(len(nums))
        ]
